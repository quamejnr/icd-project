from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from icd10.models import Category, ICD


class ICDViewsetTestCase(APITestCase):
    """ Test API endpoints of ICD """
    def setUp(self) -> None:

        self.category = Category.objects.create(code='A1', title='Cholera')

        self.icd = ICD.objects.create(diagnosis_code = '03', abbreviated_description='Cholera due to vibrio cholerae', 
                                full_description='Cholera due to vibrio cholerae', category=self.category)

        self.data = {
            "diagnosis_code": "01",
            "abbreviated_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
            "full_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
            "category": self.category.id
        }

        return super().setUp()


    def test_create_icd(self) -> None:
        """Test create view of icd"""
        response = self.client.post(reverse('code-list'), data=self.data, format='json')

        diagnosis_code = response.data['diagnosis_code']
        full_code = response.data['full_code']
        abbreviated_description = response.data['abbreviated_description']
        full_description = response.data['full_description']
        category = response.data['category']

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(diagnosis_code, '01')
        self.assertEqual(full_code, 'A101')
        self.assertEqual(abbreviated_description, "Cholera due to Vibrio cholerae 01, biovar cholerae")
        self.assertEqual(full_description, "Cholera due to Vibrio cholerae 01, biovar cholerae")
        self.assertEqual(category, {'code':'A1', 'title':'Cholera'})

    def test_list_icd(self) -> None:
        """Test list API view of ICD"""

        response = self.client.get(reverse('code-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_icd(self) -> None:
        """Test detail API view of ICD"""

        response = self.client.get(reverse('code-detail', args=[self.icd.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_update_icd(self) -> None:
        """Test update API view of iCD"""

        self.data.update({'diagnosis_code': "04"})

        response = self.client.put(reverse('code-detail', args=[self.icd.id]), data=self.data, format='json')
        diagnosis_code = response.data['diagnosis_code']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(diagnosis_code, '04')

    def test_delete_icd(self) -> None:
        """Test delete API view of ICD"""

        response = self.client.delete(reverse('code-detail', args=[self.icd.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def tearDown(self) -> None:
        return super().tearDown()


class CategoryViewsetTestCase(APITestCase):
    """ Test API endpoints of Category """
    def setUp(self) -> None:

        self.category = Category.objects.create(code='A1', title='Cholera')

        self.data = {
            "code": 'A2',
            "title": 'Typhoid'
        }

        return super().setUp()


    def test_create_category(self) -> None:
        """Test create view of icd categories"""
        response = self.client.post(reverse('category-list'), data=self.data, format='json')

        code = response.data['code']
        title = response.data['title']

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(code, 'A2')
        self.assertEqual(title, 'Typhoid')

    def test_list_category(self) -> None:
        """Test list API view of icd categories"""

        response = self.client.get(reverse('category-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_icd(self) -> None:
        """Test detail API view of ICD categories"""

        response = self.client.get(reverse('category-detail', args=[self.category.id]))

        code = response.data['code']
        title = response.data['title']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(code, 'A1')
        self.assertEqual(title, 'Cholera')

    def test_update_icd(self) -> None:
        """Test update API view of ICD categories"""

        self.data.update({'code': 'A3'})

        response = self.client.put(reverse('category-detail', args=[self.category.id]), data=self.data, format='json')
        diagnosis_code = response.data['code']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(diagnosis_code, 'A3')

    def test_delete_icd(self) -> None:
        """Test delete API view of ICD"""

        response = self.client.delete(reverse('category-detail', args=[self.category.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def tearDown(self) -> None:
        return super().tearDown()
        
