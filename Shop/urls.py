"""
URL configuration for Med project.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="indec"),
    path('products/', views.products, name="product"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('catalogue/', views.catalogue, name="catalogue"),
    path('signup/', views.signupView, name="signup"),
    path('login/', views.loginView, name="login"),
]
