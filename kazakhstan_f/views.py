import os
from kazakhstan_f.forms import FeedbackForm, ImageForm, LoginForm, ManagersCreateForm, SignUpForm, ToursCreateForm
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib import auth
from .models import Tours, User
from django.db.models import Q
from django.core.mail import send_mail


def home(request):
    
    return render(request, "kazakhstan_f/index.html", {})


def about(request):
    
    return render(request, "kazakhstan_f/about.html", {})

def tours(request):
    tours = Tours.objects.all()
    return render(request, "kazakhstan_f/tours.html", {'tours':tours })

def contacts(request):
    msg = None
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            text = request.POST.get('message')
            subject = request.POST.get("name")

            sendEmail('170103038@stu.sdu.edu.kz', text, 'у вас новое письмо от: ' + subject)
            msg = 'Email has been lsent! successfully!'
            return render(request, "kazakhstan_f/contact.html", {'form':form, 'msg':msg})
        else:
            msg = "form is not valid!"
        # return JsonResponse({'form_errors': form.errors, 'msg': msg})
    else:
        form = FeedbackForm()
    return render(request, "kazakhstan_f/contact.html", {'form':form})


def sendEmail(email, text, subject):
    send_mail(subject, text, 'ascienkz@gmail.com', 
        [email], fail_silently=True)


def blog(request):
    
    return render(request, "kazakhstan_f/blog.html", {})



def login_view(request):
    
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                msg = "Invalid credentials"
        else:
            msg = "error fields!"
    return render(request, "kazakhstan_f/login.html", {"form": form, "msg":msg})

def register_view(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User registered successfully!'
            login(request,user)
            return redirect('home')
    

        else:
            msg = "form is not valid!"
        # return JsonResponse({'form_errors': form.errors, 'msg': msg})
    else:
        form = SignUpForm()
    return render(request, "kazakhstan_f/register.html", {'form': form, 'msg': msg})

def logout(request):
    auth.logout(request)
    return redirect("home")

def adm(request):
    user = request.user
    if not user.is_authenticated or user.user_type == 'client':
        return redirect("adm.login")


    return render(request,"kazakhstan_f/admin/index.html")

def admLogin(request):

    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            msg = user
            if user is not None and (user.is_superuser or user.user_type != 'client'):
                login(request,user)
                return redirect('adm')
            else:
                msg = "Invalid credentials"
        else:
            msg = "error fields!"
    return render(request, "kazakhstan_f/admin/login.html", {"form": form, "msg":msg})


def admLogout(request):

    auth.logout(request)
    return redirect("adm.login")


def managers(request):
    user = request.user
    if not user.is_authenticated or user.user_type == 'client':
        return redirect("adm.login")

    managers = User.objects.filter(is_superuser=False).filter(~Q(user_type='client'))

    
    return render(request, "kazakhstan_f/admin/managers.html", {'users': managers})

def managersCreate(request):
    user = request.user
    if not user.is_authenticated or user.user_type == 'client':
        return redirect("adm.login")

    msg = None
    if request.method == 'POST':
        form = ManagersCreateForm(request.POST)
        if form.is_valid():
            manager = form.save()

            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            text = "Добро пожаловать! \n\n Ваш логин: " + username + "\nВаш пароль: " + password
            sendEmail(email, text, "Вас зарегали как менеджер")
            msg = 'User registered successfully!'

            # return HttpResponse(text)
            return redirect('adm.managers')
        else:
            msg = "form is not valid!"

    else:
        form = ManagersCreateForm()
    # return render(request, "kazakhstan_f/register.html", {'form': form, 'msg': msg})
    return render(request, "kazakhstan_f/admin/managers_create.html", {'form': form, 'msg': msg})


def managersEdit(request, id):
    manager = User.objects.get(id=id)
    return render(request, "kazakhstan_f/admin/managers_edit.html", {'manager':manager})
    
def managersUpdate(request, id):
    manager = User.objects.get(id=id)
    manager.username = request.POST['username']
    manager.email = request.POST.get('email')
    manager.save()
    return redirect('adm.managers')


def managersDelete(request, id):
    managers = User.objects.get(id=id)
    managers.delete()
    return redirect('adm.managers')

def toursBack(request):
    user = request.user
    if not user.is_authenticated or user.user_type == 'client':
        return redirect("adm.login")
    tours = Tours.objects.all()

    return render(request, "kazakhstan_f/admin/tours.html", {'tours': tours})

def toursCreate(request):
    user = request.user
    if not user.is_authenticated or user.user_type == 'client':
        return redirect("adm.login")
    msg = None
    if request.method == 'POST':
        form = ToursCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = 'User registered successfully!'
            return redirect('adm.tours')
        else:
            msg = "form is not valid!"

    else:
        form = ToursCreateForm()
    # return render(request, "kazakhstan_f/register.html", {'form': form, 'msg': msg})
    return render(request, "kazakhstan_f/admin/tours_create.html", {'form': form, 'msg': msg})


def toursEdit(request, id):
    tour = Tours.objects.get(id=id)
    return render(request, "kazakhstan_f/admin/tours_edit.html", {'tour': tour})


def toursUpdate(request, id):

    tour = Tours.objects.get(id=id)
  
    tour.name = request.POST.get('name')
    tour.description = request.POST.get('description')
    tour.price = request.POST.get('price')
    tour.date = request.POST.get('date')
    tour.image = request.POST.get('image')
    entry = tour.save()

    form = ImageForm(request.POST, request.FILES, instance=tour)

    if form.is_valid():
        image_path = tour.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
        form.save()

    return redirect("adm.tours")
    

def toursDelete(request, id):
    tour = Tours.objects.get(id=id)
    tour.delete()
    return redirect("adm.tours")
