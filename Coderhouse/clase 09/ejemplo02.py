import json

# mi_archivo = open("mi_archivo.json", "r")
# mi_dict = json.load(mi_archivo)
# f.close()

with open("mi_archivo.json", "r") as mi_archivo:
  mi_dict = json.load(mi_archivo)

print(mi_dict)