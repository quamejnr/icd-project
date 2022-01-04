from django.test import TestCase
from icd10.models import Category, ICD

class ModelsTestCase(TestCase):
    def setUp(self) -> None:

        self.category = Category.objects.create(
            code = 'A0',
            title = 'Cholera'
        )

        self.icd = ICD.objects.create(
            diagnosis_code = '1234',
            abbreviated_description = 'Comma-induced anal retention',
            full_description = "Comma-induced anal retention",
            category = self.category
        )

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_category_model(self):
        """Test Category Model"""
        category = Category.objects.get(id=1)
        category_code = category.code
        category_title = category.title

        self.assertEqual(category_code, 'A0')
        self.assertEqual(category_title, 'Cholera')

    def test_icd_model(self):
        """Test ICD Model"""
        icd = ICD.objects.get(diagnosis_code='1234')
        diagnosis_code = icd.diagnosis_code
        full_code = icd.full_code
        abbreviated_description = icd.abbreviated_description
        full_description = icd.full_description
        category = icd.category

        self.assertEqual(diagnosis_code, '1234')
        self.assertEqual(full_code, 'A01234')
        self.assertEqual(abbreviated_description, 'Comma-induced anal retention')
        self.assertEqual(full_description, 'Comma-induced anal retention')
        self.assertEqual(category, self.category)


