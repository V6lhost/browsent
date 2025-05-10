from django.shortcuts import render
from django.http.response import HttpResponse

shared_files = {
  0: {
    "name": "001.png",
    "type": "image"
  },
  1: {
    "name": "002.jpeg",
    "type": "image"
  },
  2: {
    "name": "001.mp4",
    "type": "video"
  }
}

def index(request):
  return render(request, "browsent/index.html", {
    "title": " | Homepage"
  })

def download(request, id):
  return HttpResponse("you cant download file: " + id + " right now")

def upload(request):
  return render(request, "browsent/upload.html", {
    "title": " | Upload"
  })

def files(request):
  return render(request, "browsent/files.html", {
    "title": " | Files that shared with you",
    "shared_files": shared_files
  })

def file(request, file):
  return render(request, "browsent/view_file.html", {
    "file": file
  })