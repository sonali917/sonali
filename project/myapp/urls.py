from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('dash', views.dash, name='dash'),
    path('<int:id>/userlist/', views.userlist, name='userlist'),
]