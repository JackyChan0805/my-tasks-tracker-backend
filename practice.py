from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

tasks =[]
task_id = 1
@app.route('/')
def hello():
    return "hello world"


@app.route('/about')
def about():
    return "about us"


@app.route('/user/<name>')
def user(name):
    return f"wecome user {name}"


@app.route('/double/<int:num>')
def double(num):
    return f"double of {num} is {num * 2}"

@app.route('/api/user')
def get_user():
    return jsonify({
        'name' : 'Jacky',
        'age' : 20,
        'city' : 'Hong Kong'
    })


@app.route('/search')
def search():
    keyword = request.args.get('keyword', '')
    limit = request.args.get('limit', 10, type=int)
    
    return jsonify({
        'keyword': keyword,
        'limit': limit,
        'results': [f'Result {i}' for i in range(limit)]
    })

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
        'done' : False
    }
    tasks.append(new_task)
    task_id += 1

    return jsonify(new_task), 201 #201 = created

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = data.get('done', task['done'])
            task['text'] = data.get('text', task['text'])
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
    

@app.route('/ping')
def pong():
    return jsonify({"pong": True})

@app.route('/add')
def add():
    a = request.args.get('a', '',type=int)
    b = request.args.get('b', '' ,type=int)

    if a is None :
        return jsonify({"error" : "missing parameter a"}),400
    
    if b is None:
        return jsonify({"error" : "missing parameter b"}),400

    return jsonify({
        "a" : a,
        "b" : b,
        "a+b": a+b
    })

@app.route('/greet/<name>')
def greet(name):
    return jsonify({"message": f"Hello {name}"})

if __name__ == '__main__':
    app.run(debug=True,port=5002)