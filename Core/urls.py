from django.urls import path
from Core import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),

    path('settings/',views.settings,name='settings'),
    path('field/add/',views.add_dynamic_field,name='add-dynamic-field'),
    path('field/delete/',views.delete_dynamic_field,name='delete-dynamic-field'),
    path('field/edit/',views.edit_dynamic_field,name='edit-dynamic-field'),

    path('employees/',views.employees,name='employees'),
    path('employee/add/',views.add_employee,name='add-employee'),
    path('employee/details/<str:eid>/',views.employee_details,name='employee-details'),
    path('employee/delete/',views.delete_employee,name='delete-employee'),
    path('employee/edit/',views.edit_employee,name='edit-employee'),

    path('employee/data/edit/',views.edit_employee_data,name='edit-employee-data'),

    # path('employee/data/edit/',views.edit_employee_data,name='edit-employee-data'),
    # path('employee/data/delete/<int:id>/',views.delete_employee_data,name='delete-employee-data'),

    path('search/employee/',views.search_employee,name='search-employee')
]