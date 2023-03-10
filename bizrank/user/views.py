from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from django.template import Context
from user.forms import UserRegisterForm


@login_required
def index(request):
    return render(request, 'index.html', {'title':'Home page'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print('post')
        if form.is_valid():
            print('form is valid')
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            messages.success(request, f'{username}, Your account has been created! You are now able to log in')
            return redirect('login_user')
        else:
            print('form is not valid')
            messages.error(request, f'Please correct the errors below')
    print('get')
    form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'title':'Sign up'})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            print('post')
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                print('user is not none')
                form = login(request, user)
                messages.success(request, f'Welcome {username} !!')
                return redirect('index')
            else:
                messages.info(request, f'This account does not exist')
        
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'Login page'})