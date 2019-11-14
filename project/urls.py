# -*- coding: utf-8 -*-
"""project URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls',)),
]

# A pattern to include the login and logout views for the browsable API.
urlpatterns += [
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')
]

# Provide a mechanism for clients to obtain a token
# given the username and password.
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
