from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Core.models import Field,Option,Employee,Employee_Details
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    context = {
        'page' : 'dashboard',
    }
    return render(request,'Core/dashboard.html',context)

#----------------------------------- SETTINGS -----------------------------------#

@login_required
def settings(request):
    fields = Field.objects.filter(Added=request.user)
    count = Employee.objects.count()
    context = {
        'fields' : fields,
        'count' : count,
        'page' : 'settings'
    }
    return render(request,'Core/settings.html',context)

#----------------------------------- ADD FIELD -----------------------------------#

@login_required
def add_dynamic_field(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        field_type = request.POST.get('type')

        Field.objects.create(Added=request.user,Field_Name=name,Field_Type=field_type)
        messages.success(request,'new field added successfully ... !')

    return redirect('settings')

#----------------------------------- DELETE FIELD -----------------------------------#

@csrf_exempt
def delete_dynamic_field(request):
    if request.method == 'POST':
        field_id = request.POST.get('id')
        field = Field.objects.get(id=field_id)
        field.delete()

        return JsonResponse({'status':'success','message':'Field Deleted Successfully ... !'})
    
#----------------------------------- EDIT FIELD -----------------------------------#

@csrf_exempt
def edit_dynamic_field(request):
    if request.method == 'POST':
        field_id = request.POST.get('id')
        field = Field.objects.get(id=field_id)
        field.Field_Name = request.POST.get('name')
        field.Field_Type = request.POST.get('type')
        field.save()

        return JsonResponse({'status':'success','message':'Field Edited Successfully ... !'})

#----------------------------------- EMPLOYEES -----------------------------------#

@login_required
def employees(request):
    employees = Employee.objects.filter(Added=request.user).order_by('-id')
    fields = Field.objects.filter(Added=request.user)
    context = {
        'page' : 'employees',
        'employees' : employees,
        'fields' : fields
    }
    return render(request,'Core/employees.html',context)

#----------------------------------- ADD EMPLOYEE -----------------------------------#

@login_required
def add_employee(request):
    fields = Field.objects.filter(Added=request.user)
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        datas = request.POST.getlist('data[]')

        try:
            employee = Employee.objects.create(
                Added=request.user,First_Name=fname,Last_Name=lname,Email=email,Mobile=mobile
            )

            for field, data in zip(fields, datas):
                Employee_Details.objects.create(Employee=employee,Field=field,Data=data)

            messages.success(request,'new employee added successfully ... !')
        except:
            messages.warning(request,"something went wrong can't create employee ... !")

        return redirect('employees')
    
#----------------------------------- EMPLOYEE DETAILS -----------------------------------#

@login_required
def employee_details(request,eid):
    employee = Employee.objects.get(id=eid)
    datas = Employee_Details.objects.filter(Employee=employee)

    fields = Field.objects.filter(Added=request.user)

    for field in fields:
        Employee_Details.objects.get_or_create(Employee=employee, Field=field)

    context = {
        'page' : 'employees',
        'employee' : employee,
        'datas' : datas
    }
    return render(request,'Core/employee.html',context)

#----------------------------------- DELETE EMPLOYEE -----------------------------------#

@csrf_exempt
def delete_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('id')
        employee = Employee.objects.get(id=employee_id)
        employee.delete()
        return JsonResponse({'status':'success','message':'Field Deleted Successfully ... !'})

#----------------------------------- EDIT EMPLOYEE -----------------------------------#

@csrf_exempt
def edit_employee(request):
    if request.method == 'POST':
        eid = request.POST.get('eid')

        employee = Employee.objects.get(id=eid)

        employee.First_Name = request.POST.get('fname')
        employee.Last_Name = request.POST.get('lname')
        employee.Email = request.POST.get('email')
        employee.Mobile = request.POST.get('mobile')

        employee.save()
        return JsonResponse({'status':'success'})
    
#----------------------------------- EDIT EMPLOYEE DATA -----------------------------------#

@csrf_exempt
def edit_employee_data(request):
    if request.method == 'POST':
        data_id = request.POST.get('id')
        data = Employee_Details.objects.get(id=data_id)
        data.Data = request.POST.get('data')
        data.save()
    return JsonResponse({'status':'success'})

#----------------------------------- SEARCH EMPLOYEE -----------------------------------#

@csrf_exempt
def search_employee(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        if query is not None:

            result = result = Employee.objects.filter(Added=request.user).filter(
                Q(First_Name__icontains=query) |
                Q(Last_Name__icontains=query) |
                Q(Email__icontains=query) |
                Q(Mobile__icontains=query)
            ).order_by('-id')

            data = list(result.values())
            return JsonResponse({'status': 'success', 'result': data})
        else:
            return JsonResponse({'status': 'error', 'message': 'No query parameter provided'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'}, status=405)