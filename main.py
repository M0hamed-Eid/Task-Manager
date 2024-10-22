from flask import Flask
from controllers.users_controller import users_controller
from controllers.task_update_delete import tasks_controller

app = Flask(__name__)



app.register_blueprint(users_controller)
app.register_blueprint(tasks_controller)


    


if __name__ == '__main__':
    app.run(debug=True)