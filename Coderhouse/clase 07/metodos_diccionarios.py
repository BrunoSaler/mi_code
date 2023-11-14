dict_1 = {"harry": "potter", "frodo": "baggins"}

print(dict_1["frodo"])
# print(dict_1["bilbo"]) # da error "KeyError"
print(dict_1.get("bilbo"))#en vez de romperse da none
print(dict_1.get("bilbo", "Bolsón"))#si encuentra la key devuelve el valor, sino el segundo argumento
print(dict_1.get("harry"))