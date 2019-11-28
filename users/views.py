from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout, login, authenticate
from users.forms import register_users
from django.contrib.auth.models import User
from users.models import InformationUsers
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.


def welcome(request):
    return render(request, "users/welcome.html")


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff is not False:
                return redirect(reverse_lazy('admin:index')) #acordar lo de app_name para la ruas
            else:
                return redirect(reverse_lazy('home'))
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    if request.user.is_active:
        return redirect(reverse_lazy('home'))
    else:
        return render(request, "users/login.html")


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect(reverse_lazy('home'))


def register(request):
    if request.method == 'POST':
         # Añadimos los datos recibidos al formulario
        form = register_users(request.POST)
        if form.is_valid():
          
            username = request.POST.get('username', None)
            first_name = request.POST.get('first_name', None)
            last_name = request.POST.get('last_name', None)
            email = request.POST.get('email', None)
            briday_Date = request.POST.get('briday_Date', None)
            password1 = request.POST.get('password1', None)
            try:
                newuser = User(username=username, first_name=first_name,last_name=last_name, email=email)
                newuser.set_password(password1)
                newuser.save()
                newinformation_users = InformationUsers(user=newuser, briday_date=briday_Date, imagen=None)
                newinformation_users.save()
                messages.success(request, 'Registro exitoso.')
                form = register_users()
            except:
                newuser.delete()
                newinformation_users.delete()
                messages.error(request, 'Ocurrio un error.')
            
    else:
        form = register_users()
    return render(request, 'users/register.html', {'form': form})
