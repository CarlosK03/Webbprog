from django.urls.resolvers import URLPattern


from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path("", views.tasklist1, name="tasklist1"),
    path("add/", views.add, name="add"),
]