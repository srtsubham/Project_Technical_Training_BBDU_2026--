from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.models import User

def index(r):
    return render(r, 'index.html')

def products(r):
    return render(r, 'products.html')

def about(r):
    return render(r, 'about.html')

def contact(r):
    if r.method == "POST":
        n = r.POST.get('name')
        p = r.POST.get('phone')
        e = r.POST.get('email')
        m = r.POST.get('msg')
        o = Contact(name=n, phone=p, emailid=e, msg=m)
        o.save()
        return redirect('/contact/')
    d = Contact.objects.all()
    return render(r, 'contact.html', {'data': d})

def catalogue(r):
    return render(r, 'catalogue.html')

def signupView(r):
    if request.method == "POST":

        m5 = r.POST.get('emailAddress')
        m6 = r.POST.get('username')
        m7 = r.POST.get('password')
        o = Contact(emailAddress=m5, username=m6, password=m7)
        o.save()
        return redirect('/signup/')
        if password==cpassword:
            user = User.objects.create_user(emailAddress, username, password)
            user.first_name = firstName
            user.last_name = lastName
            user.save()
            return redirect('/signup/')
    return render(r, 'signup.html')

def loginView(r):
    if request.method == "POST":

    return render(r, 'login.html')
