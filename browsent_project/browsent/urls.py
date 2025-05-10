from django.urls import path
from . import views

urlpatterns = [
  path("", views.index),
  path("index", views.index),
  path("download/<str:id>", views.download, name="download"),
  path("upload", views.upload),
  path("files", views.files),
  path("file", views.file)
]