from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='member_login'),
    path('registration/', views.register, name='member_register')
]