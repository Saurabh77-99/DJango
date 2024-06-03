from django.contrib import admin
from django.urls import path
from . import views

# app/route
urlpatterns = [
    path('',views.app,name='app'),
    # path('route/',views.route,name='route'),
]