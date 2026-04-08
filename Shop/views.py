from django.shortcuts import render, redirect
from .models import Contact

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
