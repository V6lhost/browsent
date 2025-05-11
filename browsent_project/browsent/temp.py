import os

class TemporaryFileManager:
  def __init__(self, base_path: str = "/tmp"):
    self.path = os.path.join(base_path, "browsent")
    os.makedirs(self.path, exist_ok=True)

  def add_file(self, name: str, data: bytes) -> str:
    file_path = os.path.join(self.path, name)
    if os.path.exists(file_path):
      raise FileExistsError("File already exists, try renaming.")
    with open(file_path, "wb") as f:
      f.write(data)
    return(file_path)
  
  def add_file_from_path(self, local_file_path: str, name: str = None):
    name = name or os.path.basename(local_file_path)
    with open(local_file_path, "rb") as f:
      data = f.read()
    return(self.add_file(name, data))
  
  #note: there is a problem which decreases download speeds
  def read_file(self, name: str) -> bytes:
    file_path = os.path.join(self.path, name)
    if not os.path.exists(file_path):
      raise FileNotFoundError("File not found on shared files")
    with open(file_path, "rb") as f:
      return f.read()

  #temporary solution: just use a function for return full file path and use open function in views.py
  def return_file_path(self, name: str) -> str:
    return os.path.join(self.path, name)

  
  def delete_file(self, name: str):
    file_path = os.path.join(self.path, name)
    if os.path.exists(file_path):
      os.remove(file_path)
  
  def list_files(self):
    files = os.listdir(self.path)
    files_with_size = dict()
    for file in files:
      file_path = os.path.join(self.path, file)
      size = os.path.getsize(file_path)
      files_with_size[file] = str(size) + " Bytes"
    
    return files_with_size
