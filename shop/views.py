from django.shortcuts import render

# Create your views here.

def home(request):
    print('entered into home')
    return render(request,'Pages/HomePage.html')

def signup(request):
    return render(request,'Pages/SignupPage.html')

def loginup(request):
    return render(request,'Pages/LoginPage.html')

def shop(request):
    return render(request,'Pages/ShopPage.html')

def contactus(request):
    return render(request,'Pages/ContactusPage.html')
    
def aboutus(request):
    return render(request,'Pages/AboutusPage.html')