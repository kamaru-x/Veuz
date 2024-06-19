from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Core.models import Employee,Additional_Details
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    context = {
        'page' : 'dashboard',
    }
    return render(request,'Core/dashboard.html',context)

#----------------------------------- EMPLOYEES -----------------------------------#

@login_required
def employees(request):
    employees = Employee.objects.all().order_by('-id')
    context = {
        'page' : 'employees',
        'employees' : employees
    }
    return render(request,'Core/employees.html',context)

#----------------------------------- ADD EMPLOYEE -----------------------------------#

@login_required
def add_employee(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        try:
            Employee.objects.create(First_Name=fname,Last_Name=lname,Email=email,Mobile=mobile)
            messages.success(request,'new employee added successfully ... !')
        except:
            messages.warning(request,"something went wrong can't create employee ... !")

    return redirect('employees')

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
    
#----------------------------------- ADD EMPLOYEE DATA -----------------------------------#

@csrf_exempt
def add_employee_data(request):
    if request.method == 'POST':
        eid = request.POST.get('eid')
        employee = Employee.objects.get(id=eid)

        title = request.POST.get('title')
        data = request.POST.get('data')

        d = Additional_Details.objects.create(Employee=employee,Field_Name=title,Data=data)

        return JsonResponse({'status':'success','data_id':d.id})
    
#----------------------------------- EDIT EMPLOYEE DATA -----------------------------------#

@csrf_exempt
def edit_employee_data(request):
    if request.method == 'POST':
        data_id = request.POST.get('data_id')
        data = Additional_Details.objects.get(id=data_id)
        data.Data = request.POST.get('data')
        data.save()
    return JsonResponse({'status':'success'})
    
#----------------------------------- DELETE EMPLOYEE DATA -----------------------------------#

@login_required
def delete_employee_data(request,id):
    data = Additional_Details.objects.get(id=id)
    emp = data.Employee
    data.delete()
    return redirect('settings',emp.id)

#----------------------------------- DELETE EMPLOYEE -----------------------------------#

@login_required
def delete_employee(request,eid):
    employee = Employee.objects.get(id=eid)
    employee.delete()
    messages.warning(request,'deleted employee successfully ... !')
    return redirect('employees')

#----------------------------------- SETTINGS -----------------------------------#

@login_required
def settings(request,eid):
    employee = Employee.objects.get(id=eid)
    datas = Additional_Details.objects.filter(Employee=employee)
    context = {
        'page' : 'employees',
        'employee' : employee,
        'datas' : datas
    }
    return render(request,'Core/settings.html',context)

#----------------------------------- SEARCH EMPLOYEE -----------------------------------#

@csrf_exempt
def search_employee(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        if query is not None:
            result = Employee.objects.filter(First_Name__icontains=query).order_by('-id')
            data = list(result.values())
            return JsonResponse({'status': 'success', 'result': data})
        else:
            return JsonResponse({'status': 'error', 'message': 'No query parameter provided'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'}, status=405)