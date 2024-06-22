from django.contrib import admin
from Core.models import Field,Option,Employee,Employee_Details

# Register your models here.

@admin.register(Field)
class FieldModelAdmin(admin.ModelAdmin):
    list_display = ['Added','Field_Name','Field_Type']

@admin.register(Option)
class OptionModelAdmin(admin.ModelAdmin):
    list_display = ['Field','Value']

@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['Added','First_Name','Last_Name','Email','Mobile']

@admin.register(Employee_Details)
class EDetailsModelAdmin(admin.ModelAdmin):
    list_display = ['Employee','Field','Data']