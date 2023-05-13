from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns =[
    path('checkEmail',views.check_email),
    path('checkUsername',views.checkUsername),
    path('email/:token',views.email_token),
    path('login',views.login),
    path('refreshToken',views.refreshToken),
    path('register',views.register),
]





