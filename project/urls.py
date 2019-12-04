# -*- coding: utf-8 -*-
"""project URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
	path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls',)),

	# A pattern to include the login and logout views for the browsable API.
	path('api-auth/', include('rest_framework.urls')),

	# Provide a mechanism for clients to obtain a token
	# given the username and password.
    path('api-token-auth/', views.obtain_auth_token),
]
