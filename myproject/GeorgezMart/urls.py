from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Maps the base URL for the app to the "home" view
    path('customers/', views.customer_list, name='customer_list'),
  
]
