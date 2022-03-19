from django.contrib import admin
from icd10.models import ICD, Category


# Register your models here.
admin.site.register(ICD)
# admin.site.register(Category)

class ICDAdmin(admin.StackedInline):
    model = ICD
    

@admin.register(Category)
class Category(admin.ModelAdmin):
    inlines = [ICDAdmin]
    
