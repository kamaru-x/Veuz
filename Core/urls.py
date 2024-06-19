from django.urls import path
from Core import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),

    path('employees/',views.employees,name='employees'),
    path('employee/add/',views.add_employee,name='add-employee'),
    path('employee/edit/',views.edit_employee,name='edit-employee'),
    path('employee/delete/<int:eid>/',views.delete_employee,name='delete-employee'),

    path('employee/data/add/',views.add_employee_data,name='add-employee-data'),
    path('employee/data/edit/',views.edit_employee_data,name='edit-employee-data'),
    path('employee/data/delete/<int:id>/',views.delete_employee_data,name='delete-employee-data'),

    path('settings/<str:eid>/',views.settings,name='settings'),

    path('search/employee/',views.search_employee,name='search-employee')
]