from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from U_Auth.models import User
from django.contrib.auth import update_session_auth_hash

# Create your views here.

#------------------------------------------------- SIGN IN ---------------------------------------------------#

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'incorrect username or password')
            return redirect('.')
    return render(request,'Auth/sign-in.html')

#------------------------------------------------- REGISTER ---------------------------------------------------#

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'A user with the same email already exists.')
            return redirect('register')  
        
        if password != cpassword:
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('register')  
        
        user = User.objects.create_user(first_name=name, username=email, email=email, password=password)

        login(request, user)
        return redirect('dashboard')
    
    return render(request, 'Auth/register.html')

#----------------------------------------------CHANGE PASSWORD -----------------------------------------------#

@login_required
def changepassword(request):
    user = request.user
    if request.method == 'POST':
        currentPassword = request.POST.get('currentPassword')
        newPassword = request.POST.get('newPassword')
        confirmPassword = request.POST.get('confirmPassword')

        if not user.check_password(currentPassword):
            messages.error(request, 'Incorrect current password')
            return redirect('change-password')
        elif newPassword != confirmPassword:
            messages.error(request,'Password and confirm password does not match try again')
            return redirect('change-password')
        else:
            user.set_password(confirmPassword)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request,'Password changed login again')
            return redirect('dashboard')
        
    return render(request,'Auth/change-password.html')

#------------------------------------------------- SIGN OUT --------------------------------------------------#

@login_required
def signout(request):
    logout(request)
    return redirect('sign-in')

#------------------------------------------------- PROFILE ---------------------------------------------------#

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')
    return render(request,'Auth/profile.html')