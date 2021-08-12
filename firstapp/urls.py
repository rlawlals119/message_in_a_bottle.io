from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('read/<str:id>',read,name="read"),
    path('create/',create,name="create"),
    path('write/',write,name="write"),
    path('update/',update,name="update"),
]