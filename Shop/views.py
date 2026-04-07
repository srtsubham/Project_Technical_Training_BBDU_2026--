from django.shortcuts import render,HttpResponse,redirect

from .models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
def products(request):
    return render(request,'products.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        emailid = request.POST.get('email')
        msg = request.POST.get('msg')
        contact = Contact(name=name, phone=phone, emailid=emailid, msg=msg)
        contact.save()
        return redirect('/contact/')

    return render(request,'contact.html')
def catalogue(request):
    return render(request,'catalogue.html')
