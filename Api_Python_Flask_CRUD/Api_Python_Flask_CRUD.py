# El siguiente software es una API sencilla con la libreria flask
# el software crea una api crud con python
# Usando la librerias cv2, numpy y dlib y sus datos
# En el terminal de comandos importar librerias con el comando PIP 
# pip install flask
# pip 25.1.1
# Python 3.13.1

from flask import Flask, jsonify, request
app = Flask(__name__)

# Se deja la ruta de la pagina inicial
@app.route('/')
def root():
    return "Inicio de la aplicacion web"

# Se ingresa un id a la ruta usuario y se guarda una variable que tambien puede ser un insert a la base de datos
@app.route("/usuarios/<id_usuario>")
def get_user(id_usuario):
    usuario = {"id": id_usuario, "nombre":"prueba", "telefono": "12345"}
    query = request.args.get("query")
    sql = "INSERT id, nombre, telefono VALUES ",id_usuario,"prueba, 12345"
    if query:
        usuario["query"] = query
    return jsonify(usuario), 200

# En esta ruta se puede cambiar de estado una variable
@app.route("/usuarios", methods=["POST"])
def create_usuario():
    data = request.get_json()
    sql = "UPDATE * SET variables WHERE "
    data["status"] = "usuario creado"
    return jsonify(data), 201 

# En la siguiente ruta de la api se puede eliminar un usuario, pasando su id
@app.route("/usuarios/eliminar/<id_usuario>", methods=["DELETE"])
def eliminar_usuario(id_usuario):
    sql = "DELETE * FROM ", id_usuario   
    return {'ELIMINADO': 'Id eliminado'}


if __name__=="__main__":
    app.run(debug=True)