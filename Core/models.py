from django.db import models
from U_Auth.models import User

# Create your models here.

class Employee(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100,null=True)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.First_Name
    
class Additional_Details(models.Model):
    Employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    Field_Name = models.CharField(max_length=100)
    Data = models.TextField()

    def __str__(self):
        return f'{self.Employee} | {self.Field_Name}'