from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError, transaction
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import ProfileForm, UserForm
from django.template.defaulttags import csrf_token
from .models import NewsDB
from .models import LattersToRector


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'myapp/html/signupuser.html', {'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentmyapp')
            except IntegrityError:
                return render(request, 'myapp/html/signupuser.html', {'form':ProfileForm(), 'name_error':'Такое имя уже существует!'})
        else:
            return render(request, 'myapp/html/signupuser.html', {'form':ProfileForm(), 'pass_error':'Пароли не совподают!'})

def currentmyapp(request):
    return render(request, 'myapp/html/currentmyapp.html')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('settings:profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def profileuser(request):
    return render()

def signinuser(request):
    if request.method == 'GET':
        return render(request, 'myapp/html/signinuser.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'myapp/html/signinuser.html', {'form':AuthenticationForm, 'error':'Пользователь не найден! Может быть неверный Логин или пароль?'})
        else:
            login(request, user)
            return redirect('newsstud')

def signoutuser(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'myapp/html/signinuser.html')

def newsstud(request):
    news = NewsDB.objects.all()
    return render(request, 'myapp/html/newsstud.html', {'news':news})

def lattertorector(request):
    latters = LattersToRector.objects.all()
    return render(request, 'myapp/html/lattertorector.html', {'latters':latters})

def profileupdateuser(request):
    return render()

def createlattertorector(request):
    if request.method == 'POST':
        try:
            later = LattersToRector()
            later.title = request.POST.get('title')
            later.content = request.POST.get('content')
            later.username = request.POST.get('username')
            later.save()
            return render(request, 'myapp/html/lattertorector.html', {'success':'Письмо было отправлено!'})
        except:
            return render(request, 'myapp/html/createlattertorector.html', {'error':'Произошла ошибка!'})
    else:
        return render(request, 'myapp/html/createlattertorector.html')


def somenewsbig(request):
    return render()

def home(request):
    return redirect('signinuser')