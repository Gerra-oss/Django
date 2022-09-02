from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url ='login')
def index(request):
    return render(request, "home.html", {'Title' : 'Site api Home page'} )

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(request, username = username, password = password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, "index.html", {'Title' : 'Site api Login'})

def logout(request):
    auth.logout(request)
    return redirect('login')

@requires_csrf_token
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        user  = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                print("user name taken")
            elif User.objects.filter(email = email).exists():
                print("email exists")
        user.save()
        return redirect('login')


    return render(request, "register.html", {'Title' : 'Site api Registration'})

def api_list(request):
    pass

def detail(request):
    pass
