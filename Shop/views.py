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
