from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from Api.serializers import UserSerializer,EmployeeSerializer
from U_Auth.models import User
from Core.models import Employee
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# ------------------------------------------------------- CLASS BASED API VIEWS ----------------------------------- #

class EmployeeListCreate(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(Added=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(Added=self.request.user)
        else:
            print(serializer.error)

class EmployeeDelete(generics.DestroyAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(Added=user)
    
class EmployeeUpdate(generics.UpdateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(Added=user)

# ----------------------------------------------- FUNCTION BASED API VIEWS ----------------------------------- #

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def employee(request, id=None):
    if request.method == 'GET':
        employees = Employee.objects.filter(Added=request.user)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Added=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT' or request.method == 'PATCH':
        try:
            employee = Employee.objects.get(id=id, Added=request.user)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            employee = Employee.objects.get(id=id, Added=request.user)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)