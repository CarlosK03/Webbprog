from django.urls.resolvers import URLPattern


from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from Register import views as v
urlpatterns = [
    path('', views.cool, name="cool"),
    path('brian/', views.brian, name="brian"),   
    path("about/", views.about , name="about"),
    path("contact/", views.contact , name="contact"),
    path("frst/", views.frst , name="frst"),
]