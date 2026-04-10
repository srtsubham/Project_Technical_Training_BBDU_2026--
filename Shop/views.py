from django.contrib.auth import authenticate, login, logout
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
    if r.method == "POST":
        m5 = r.POST.get('emailAddress')
        m6 = r.POST.get('username')
        m7 = r.POST.get('password')

        if m6 and m7:
            u = User.objects.create_user(username=m6, email=m5, password=m7)
            u.save()
            return redirect('/login/')
        else:
            return render(r, 'signup.html', {"error": "Valid data required"})

    return render(r, 'signup.html')

def loginView(r):
    if r.method == "POST":
        u = r.POST.get('userName')
        p = r.POST.get('password')
        v = authenticate(username=u, password=p)
        if v is not None:
            login(r, v)
            return redirect('/')
        else:
            return render(r, "login.html", {"error":"Username or Password is incorrect."})
    return render(r, 'login.html')

def logoutView(r):
    logout(r)
    return redirect('/login/')
