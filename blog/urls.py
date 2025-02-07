from django.urls import path

from . import views

urlpatterns = [path("", views.index),
              
               path("createpost/", views.createpost, name="createpost"),
               path("getpost/", views.getpost, name="getpost"),
                path("singlepost/", views.singlepost, name="singlepost"),
               path("deletepost/", views.deletepost, name="deletepost"),
               path("updatepost/", views.updatepost, name="updatepost")
               ]
