import json

class Locker:
  def __init__(self, file_name):
    if ".json" in file_name:
      self.filename = file_name
    else:
      self.filename = file_name + ".json"
    insta = {}
    with open(self.filename, "w") as f:
      json.dump(insta, f)
  
  def add(self, Key, Value):
    with open(self.filename) as x:
      Data = json.load(x)
    Data[Key] = Value
    with open(self.filename, "w") as x:
      json.dump(Data, x)

  def view(self, Key):
    with open(self.filename) as x:
      Data = json.load(x)
    return Data[Key]
