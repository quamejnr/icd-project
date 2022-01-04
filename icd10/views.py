import csv
from icd10.notification_service.event import notify
from icd10.notification_service.listener import EmailListener
import os
from rest_framework import status
from icd10.models import Category, ICD
from rest_framework import viewsets
from icd10.serializers import CategorySerializer, ICDSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction


# Initialize event listeners
EmailListener()


class CategoryViewset(viewsets.ModelViewSet):
    """Viewset for creating, retrieving, updating and deleting Categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ICDViewset(viewsets.ModelViewSet):
    """Viewset for creating, retrieving, updating and deleting ICD codes."""

    # reduce the number of database queries
    # by getting all related objects in a single database query
    queryset = ICD.objects.select_related('category')

    serializer_class = ICDSerializer


class FileUploadSuccessResponse(Response):
    """Extend Response class to run function after returning response. """
    def __init__(self, data, post_response_func, post_response_func_args, **kwargs):
        super().__init__(data, **kwargs)
        self.post_response_func = post_response_func
        self.post_response_func_args = post_response_func_args

    def close(self):
        super().close()
        self.post_response_func(*self.post_response_func_args)


class FileUploadView(CreateAPIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        FILE_HANDLERS = {
            '.csv': self.handle_csv_upload
        }

        # Get file extension
        file = request.FILES['file']
        file_name, file_extension = os.path.splitext(file.name)

        try:            
            file_handler = FILE_HANDLERS[file_extension]
            file_handler(file)
        
        except KeyError:
            return Response({"message":'File extension not supported'}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        
        except Exception as e:
            return Response({"message": f"Unable to upload file, something went wrong, {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return FileUploadSuccessResponse(
            {'message': 'File uploaded successfully'}, 
            post_response_func=notify, post_response_func_args=['file upload', file.name, request.user.email], 
            status=status.HTTP_201_CREATED
        )

    @transaction.atomic
    def handle_csv_upload(self, csv_file) -> None:
        csv_file =csv_file.read().decode('utf-8').splitlines()
        data = csv.reader(csv_file)

        categories = {category.code: category for category in Category.objects.all()}

        icd_codes = []   
        for row in data:
            
            # Unpack row into various headings
            category_code, diagnosis_code, full_code, abbreviated_description, full_description, category_title = row

            # Check if category in categories dictionary and create the category object when absent
            # This is better than using get_or_create method as it reduces database queries
            category = categories.get(category_code)
            if not category:
                category = Category.objects.create(code=category_code, title=category_title)
                categories[category_code] = category

            icd = ICD(
                diagnosis_code= diagnosis_code,
                full_code= full_code,
                abbreviated_description= abbreviated_description,
                full_description= full_description,
                category= category
            )
            icd_codes.append(icd)

            # Create ICD codes in batches of 10,000 to avoid memory issues
            if len(icd_codes) > 10000:
                ICD.objects.bulk_create(icd_codes)
                icd_codes.clear()

        if icd_codes:
            ICD.objects.bulk_create(icd_codes)