from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='HomePage'),
    path('/login',views.login,name="LoginPage"),
    path('/Signup',views.signup,name="SignupPage"),
    path('/Shop',views.shop,name="ShopPage"),
    path('/Aboutus',views.aboutus,name="AboutusPage"),
]