from django.urls import path
from Api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    # url endpoints user registration, login
    path('user/register/',views.CreateUserView.as_view(),name='api-user-registration'),
    path('user/token/',TokenObtainPairView.as_view(),name='get-token'),
    path('user/token/refresh/', TokenRefreshView.as_view(),name='refresh-token'),

    # class based api views for employee crud operations
    path('employees/',views.EmployeeListCreate.as_view(),name='api-employees'),
    path('employees/delete/<int:id>/',views.EmployeeDelete.as_view(),name='api-employee-delete'),
    path('employees/edit/<int:id>/', views.EmployeeUpdate.as_view(), name='employee-update'),

    # function based view for employee crud operations
    path('emps/', views.employee, name='emp-crud'),
    path('emp/<int:id>/', views.employee, name='emp-details'),
]