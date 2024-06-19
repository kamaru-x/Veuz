from django.contrib import admin
from U_Auth.models import User

# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username','id','first_name','email']