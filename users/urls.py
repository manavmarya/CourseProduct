from django.urls import path
from .views import view_register

app_name = 'users'
urlpatterns = [
                path('register/', view_register, name='view_register'), #register_view with bootstrapped template 
                
              ]