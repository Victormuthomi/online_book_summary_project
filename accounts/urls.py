from django.urls import path, include

from .import views

app_name = 'accounts'

urlpatterns=[
    #include djanongo auth urls
    path('', include('django.contrib.auth.urls')),
    #The user registration page
    path('register/', views.register, name='register'),
]