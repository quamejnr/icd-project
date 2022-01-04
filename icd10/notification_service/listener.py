from .event import subscribe
from abc import ABC, abstractmethod
from django.core.mail import send_mail
from django.conf import settings


class Listener(ABC):

    def __init__(self):
        self.setup_event_handler()

    @abstractmethod
    def setup_event_handler(self):
        pass


class EmailListener(Listener):

    def handle_file_upload(self, file_name, user_email):
        """Send user email notification after file upload"""

        send_mail(
            subject='File Upload Successful',
            message=f'File {file_name} was successfully uploaded',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user_email],
            fail_silently=False
        )

    def setup_event_handler(self):
        subscribe('file upload', self.handle_file_upload)