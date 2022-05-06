import json
from flask import request
from flask import Flask, jsonify
app = Flask(__name__)


todos = [ { "label": "My first task", "done": False } ]


@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)