
from flask import Flask, request, jsonify

from service.TaskService import TaskService

app = Flask(__name__)

service = TaskService()

@app.route("/api/tareas", methods=['GET'])
def get_tasks():
    return jsonify(service.get_task())

@app.route("/api/tareas", methods=['POST'])
def add_tasks():
    data = request.get_json()
    print(data)

    service.add_task(data)
    return jsonify({"message": "Tarea agregada exitosamente"}), 201

@app.route("/api/tareas/<string:id>", methods=['GET'])
def get_task_by_id(id):
    task = service.get_by_id(id)
    if task:
        return jsonify(task)
    else:
        return jsonify({"error": "tarea no encontrada"}), 400

@app.route("/api/tareas/<string:id>", methods=['DELETE'])
def dell_task(id):
    result = service.remove_task(id)
    print(result)
    if result is None:
        return jsonify({"mensaje":"se borro correctamente"}), 201
    else:
        return jsonify({"error":"algo salio mal"}), 201


@app.route("/api/tareas/<string:id>", methods=['PUT'])
def update_tasks(id):
    data = request.get_json()
    update = service.update_task(id,data)
    if update:
        return jsonify(update)
    else:
        return jsonify({"error":"no se pudo actualizar"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)