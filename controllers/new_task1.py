from flask import Flask , request , json 
from new_task3 import *
from new_task2 import *
app = Flask(__name__)
app.debug = True

@app.route('/')
def view():
    return json.dumps({'result':'welcome'})


@app.route('/create/task', methods=['POST'])
def createTask():
    if 'created_by' and 'assigned_to' and 'header' and 'description' and 'status' in request.form:
        created_by = request.form['created_by']
        assigned_to = request.form['assigned_to']
        header = request.form['header']
        description = request.form['description']
        status = request.form['status']
        validation_function = validateParams(created_by,assigned_to,header,description,status)
        if validation_function:
            insertTask(conn,created_by,assigned_to,header,description,status)
            return json.dumps({'rezult':'task created'})








































if __name__ == '__main__':
    app.run()