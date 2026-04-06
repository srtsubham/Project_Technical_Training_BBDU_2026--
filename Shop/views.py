from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def products(request):
    return render(request,'products.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def catalogue(request):
    return render(request,'catalogue.html')
