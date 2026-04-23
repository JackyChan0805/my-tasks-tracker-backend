from flask import Flask, jsonify, request
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

tasks =[]
task_id = 1

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_tasks():
    global task_id
    
    data = request.get_json()

    new_task = {
        'id' : task_id,
        'text' : data.get('text',''),
        'done' : False,
        'createdAt' : int(time.time() * 1000),
        'completedAt' : None,
        'timeSpent': None
    }
    tasks.append(new_task)
    task_id += 1

    return jsonify(new_task), 201 #201 = created

@app.route('/api/tasks/<int:task_id>', methods  =['PUT'])
def update_task(task_id):
    data = request.get_json()

    for task in tasks:
        if task['id'] == task_id:
            #update text
            if 'text' in data:
                task['text'] = data['text']
            #updata done status
            if 'done' in data:
                task['done'] = data['done']
                if data['done'] is True and task['completedAt'] is None:
                    task['completedAt'] = int(time.time() * 1000)
                elif data['done'] is False:
                    task['completedAt'] = None
            if 'timeSpent' in data:
                task['timeSpent'] = data['timeSpent']
            return jsonify(task)
        
    
    return jsonify({'error': 'Task not found'}), 404


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(i)
            return jsonify({'message': 'Task deleted'})
    return jsonify({'error' : 'task not found'}) , 404

if __name__ == '__main__':
    app.run(debug=True,port=5001)