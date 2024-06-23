from django.db import models
from U_Auth.models import User

# Create your models here.

class Field(models.Model):
    Added = models.ForeignKey(User,on_delete=models.CASCADE)
    Field_Name = models.CharField(max_length=225)
    Field_Type = models.CharField(max_length=20)

    def __str__(self):
        return self.Field_Name
    
class Option(models.Model):
    Field = models.ForeignKey(Field,on_delete=models.CASCADE)
    Value = models.CharField(max_length=225)

class Employee(models.Model):
    Added = models.ForeignKey(User,on_delete=models.CASCADE)

    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100,null=True)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.First_Name
    
class Employee_Details(models.Model):
    Employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    Field = models.ForeignKey(Field,on_delete=models.CASCADE)
    Data = models.TextField(null=True)

    def __str__(self):
        return f'{self.Employee} | {self.Field}'