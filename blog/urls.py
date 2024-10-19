from django.urls import path

from . import views

urlpatterns = [path("", views.index),
               path("getpost/", views.getpost, name="getpost"),
               path("createpost/", views.createpost, name="createpost"),
               ]
