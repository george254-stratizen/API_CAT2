from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Customer

def home(request):
 return render(request, 'home.html')  # Render the template

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})