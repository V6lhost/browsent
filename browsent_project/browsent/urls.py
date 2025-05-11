from django.urls import path
from . import views

urlpatterns = [
  path("", views.index),
  path("index", views.index),
  path("download/<str:name>", views.download, name="download"),
  path("upload", views.upload),
  path("delete/<str:name>", views.delete, name="delete"),
  path("files", views.files, name="files"),
  path("file_info/<str:file>", views.file_info, name="file_info")
]