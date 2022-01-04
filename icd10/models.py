from django.db import models

class Category(models.Model):
    code = models.CharField(max_length=10)
    title = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = ['code', 'title']


    def __str__(self) -> str:
        return f'{self.code} - {self.title}'


class ICD(models.Model):
    diagnosis_code = models.CharField(max_length=10, blank=True)
    full_code = models.CharField(max_length=15, blank=True, unique=True)
    abbreviated_description = models.TextField(max_length=100)
    full_description = models.TextField(max_length=233)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ICD'

    def save(self, *args, **kwargs):
        """ Create full_code before saving object."""
        category_code = self.category.code
        diagnosis_code = self.diagnosis_code
        
        self.full_code = category_code
        if self.diagnosis_code:
            self.full_code = category_code + diagnosis_code

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.category.code}, {self.diagnosis_code}, {self.full_code} {self.abbreviated_description}, {self.category.title}'
