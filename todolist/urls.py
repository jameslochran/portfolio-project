from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('todo-list/', views.tdview, name='tdlist'),

]
