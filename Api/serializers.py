from rest_framework import serializers
from U_Auth.models import User
from Core.models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password' : {'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','Added','First_Name','Last_Name','Email','Mobile']
        extra_kwargs = {'Added' : {'read_only':True}}