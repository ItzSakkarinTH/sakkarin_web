from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage),
    path("about/", views.aboutUS),
    path("contact/", views.contactUs),
]
