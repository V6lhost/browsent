from django.shortcuts import render
from django.http.response import HttpResponse, FileResponse, Http404
from .temp import TemporaryFileManager
from .forms import UploadFileForm

tfm = TemporaryFileManager()

def index(request):
  return render(request, "browsent/index.html", {
    "title": " | Homepage"
  })

def download(request, name):
  try:
    #data = tfm.read_file(name)
    return FileResponse(open(tfm.return_file_path(name), "rb"), content_type="application/octet-stream")
  except FileNotFoundError:
    raise Http404("File not foundd")

def upload(request):
  if request.method == "POST":
    form = UploadFileForm(request.POST, request.FILES)
    uploaded_file = request.FILES["file"]
    if form.is_valid():
      title = str(request.POST["title"])
      name = title or uploaded_file.name
      tfm.add_file(name, uploaded_file.read())
  else:
    form = UploadFileForm()
  return render(request, "browsent/upload.html", {
    "title": " | Upload a File",
    "form": form
  })

def delete(request, name):
  tfm.delete_file(name)
  return render(request, "browsent/delete.html")

def files(request):
  files = tfm.list_files()
  return render(request, "browsent/files.html", {
    "title": " | Files that shared with you",
    "files": files.items()
  })

def file_info(request, file):
  if request.method == 'POST':
    form = UploadFileForm(request.POST)
    filename = request.POST.get(filename)
    print(filename)

  return render(request, "browsent/file_info.html", {
    "file": file
  })