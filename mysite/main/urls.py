from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/",views.list, name="index"),
    path("home/", views.home, name="home"),
    path("",views.base, name="base"),
   path("create/", views.create, name="CreateNewList"),
    path("view/", views.view, name="view"),
]