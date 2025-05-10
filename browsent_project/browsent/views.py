from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
  return render(request, "browsent/index.html", {
    "title": " | Homepage"
  })

def get(request, id):
  return HttpResponse("you cant download file: " + id + " right now")

def upload(request):
  return render(request, "browsent/upload.html", {
    "title": " | Upload"
  })

def files(request):
  return render(request, "browsent/files.html", {
    "title": " | Files that shared with you"
  })