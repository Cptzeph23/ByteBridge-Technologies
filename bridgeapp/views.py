from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def services(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def services (request):
    return render(request, 'services.html')
