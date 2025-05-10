from django.urls import path
from . import views

urlpatterns = [
  path("", views.index),
  path("index", views.index),
  path("get/<str:id>", views.get),
  path("upload", views.upload),
  path("files", views.files)
]