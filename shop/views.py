from django.shortcuts import render

# Create your views here.

def home(request):
    print('entered into home')
    
    return render(request,'Pages/HomePage.html')
