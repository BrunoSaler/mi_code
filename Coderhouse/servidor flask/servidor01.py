from flask import Flask

app = Flask("mi_servidor")  #crea el servidor


@app.route("/")     #si pongo en el navegador 127.0.0.1:8182 hace esto

def home():
    return "Este es mi primer servidor! Bienvenidos"    #retorna ese string al servidosr, aca ya no hago print


app.run(debug=True, port=8182)  #lo corre en 127.0.0.1, en el puerto que le diga