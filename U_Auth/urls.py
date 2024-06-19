from django.urls import path
from U_Auth import views

urlpatterns = [
    path('sign-in/',views.sign_in,name='sign-in'),
    path('register/',views.register,name='register'),
    path('change-password/',views.changepassword,name='change-password'),
    path('sign-out/',views.signout,name='sign-out'),
    path('profile/',views.profile,name='profile'),
]