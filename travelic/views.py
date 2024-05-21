from django.shortcuts import render, redirect
from .models import TourPackage, galleryphoto, SaveEnquiry
from django.core.paginator import Paginator
# ---------------------------------------------------------------------------------
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def homepage(request):
    tourpackage1 = TourPackage.objects.all()
    paginator = Paginator(tourpackage1, 3)
    page_number = request.GET.get('page')
    tourpackage2 = paginator.get_page(page_number)
    return render(request, 'index.html', {'tourpackage':tourpackage2})

def contactpage(request):
    return render(request, 'Contact.html')

def packagepage(request):
    tourpackage1 = TourPackage.objects.all()
    return render(request, 'Package.html', {'tourpackage1':tourpackage1})

def gallerypage(request):
    photo = galleryphoto.objects.all()
    return render(request, 'Gallery.html', {'photo':photo})

def contactEnquiry(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        en = SaveEnquiry(name = name, email = email, phone = phone, message = message)
        en.save()
    return render(request, 'Contact.html')






# --------------------------------------------------------------------
# for registration

def registration(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already created!!')
                return redirect('registration')
            elif User.objects.filter(email= email).exists():
                messages.info(request, 'Email taken')
                return redirect('registration')
            else:
                user = User.objects.create_user(first_name=first_name,last_name = last_name, username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'password is not maching..')
            return redirect('registration')


        return redirect('/')
    return render(request, 'registration.html')




# ------------------------------------------------------------------------

def login_view(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


# -------------------------------------------------------------------

def logout(request):
    auth.logout(request)
    return redirect('/')