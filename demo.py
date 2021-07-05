from flask import Flask, json, render_template
from flask import jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

TodoList = []


@app.route("/", methods=['GET'])
def demo():
    return jsonify({'TodoList': TodoList})


@app.route("/add_todo", methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    ischeck = False if request.form.get('ischeck') == 'false' else True
    tid = len(TodoList)+1 if len(TodoList) > 0 else 1
    new_todo = {'title': str(todo), 'isCheck': ischeck, 'id': str(tid)}
    TodoList.append(new_todo)

    return jsonify({'TodoItem': new_todo})


@app.route("/remove_todo", methods=['DELETE'])
def remove_todo():
    tid = request.form.get('todo_id')

    for item in TodoList:
        if item['id'] == tid:
            TodoList.remove(item)
            break

    TodoCount = len(TodoList)

    return jsonify({'TodoCount': TodoCount})


@app.route("/edit_todo", methods=['PUT'])
def edit_todo():
    todo_id = request.form.get('todo_id')
    new_data = request.form.get('new_data')
    TodoList[int(todo_id)-1] = {'title': str(new_data)}
    return jsonify({'TodoList': TodoList})


@app.route("/updateStatus", methods=['PUT'])
def update_status():
    tid = request.form.get('id')
    ischeck = request.form.get('ischeck')
    ischeck = str(ischeck)
    ischeck = False if ischeck.upper() == 'FALSE' else True
    for item in TodoList:
        if item['id'] == tid:
            item['isCheck'] = ischeck
            break
    return jsonify({'TodoItem': str(item)})


if __name__ == "__main__":
    app.run(debug=True)
