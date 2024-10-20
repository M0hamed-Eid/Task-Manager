# Task Manager Project

## Objective
The goal of this project is to build a Task Manager application that allows users to create and manage tasks. Users will be able to:
- Add tasks
- Edit tasks
- Mark tasks as complete
- Delete tasks

The project uses:
- A modern HTML & CSS framework (Bootstrap) for layout and styling
- Deployment to the cloud using Render.com

---

## Project Setup & Flask Basics

1. **Create a project on GitHub:**
   - Set up a repository for version control.

2. **Open the project on Replit:**
   - Use Replit to collaborate with your team members.

3. **Create and run a Flask web server:**
   ```bash
   pip install flask
   ```
   Basic Flask app setup:
   ```python
   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def home():
       return 'Hello, Task Manager!'
   
   if __name__ == '__main__':
       app.run(debug=True)
   ```

4. **Push changes back to GitHub:**
   - Commit and push code frequently to the GitHub repository for collaboration.

---

## Web Pages with HTML & CSS

1. **Render templates and use static assets:**
   - Store HTML templates in a `templates` folder and static assets (CSS, JS, images) in a `static` folder.

2. **Create the layout of the page using HTML tags:**
   - Structure the page with semantic HTML elements such as `<header>`, `<main>`, and `<footer>`.

3. **Style the page using CSS classes, properties, and values:**
   - Link custom styles using `<link rel="stylesheet" href="/static/style.css">`.

4. **Use the Bootstrap framework:**
   - Bootstrap helps you develop quickly and responsively.
   ```html
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
   ```

---

## Dynamic Data & Cloud Deployment

1. **Render dynamic data using Jinja template tags:**
   - Pass dynamic data to the templates using Jinja syntax:
   ```html
   <ul>
       {% for task in tasks %}
           <li>{{ task.name }}</li>
       {% endfor %}
   </ul>
   ```

2. **Add an API route to return JSON:**
   ```python
   @app.route('/api/tasks', methods=['GET'])
   def get_tasks():
       tasks = Task.query.all()
       return jsonify([task.to_dict() for task in tasks])
   ```

3. **Deploy the project to Render.com:**
   - Connect your GitHub repository to Render and follow the deployment steps to deploy your Flask app.

---

## Functional & Aesthetic Improvements

1. **Add a Navbar and Footer using Bootstrap:**
   - Reuse Bootstrap components to create consistent navigation and a footer for all pages.

2. **Add `mailto:` links for buttons:**
   - Provide contact options using `mailto:` links in the footer.

3. **Make the website mobile-friendly (responsive):**
   - Use Bootstrap’s grid system and media queries for responsiveness.

4. **Refactor templates into reusable components:**
   - Break down large templates into smaller, reusable components such as navbars and footers.

---

## Naming Conventions

1. **PascalCase** for Classes:
   - Example: `TaskManager`, `UserProfile`

2. **camelCase** for Functions:
   - Example: `createTask()`, `editTask()`

3. **snake_case** for Variables:
   - Example: `task_id`, `is_completed`

---

## Project Structure

```
TaskManager/
│
├── app.py             # Main Flask application
├── models/            # SQLAlchemy models (database queries)
├── templates/         # HTML templates
├── static/            # CSS, JavaScript, and images
├── helpers/           # Utility functions
└── README.md          # Project documentation
```

- **controllers/**: Handles routes and logic (e.g., `task_controller.py`).
- **helpers/**: Utility functions (e.g., `validation_helper.py`).
- **models/**: SQLAlchemy models for interacting with the database (e.g., `task_model.py`).

---

## Services & Task Delegation

The team consists of 4 members. Here's how tasks can be divided:

1. **Backend Developer (Flask & API Integration)**:
   - Setup Flask routes and Jinja templating.
   - Create CRUD operations (Create, Read, Update, Delete) for tasks.
   - Implement the JSON API route.

2. **Frontend Developer (HTML, CSS, Bootstrap)**:
   - Design and structure web pages using HTML and Bootstrap.
   - Ensure a modern, responsive layout.

3. **Database Manager (SQLAlchemy & MySQL)**:
   - Define database models and handle SQL queries efficiently.
   - Manage migrations and schema design (tables: `tasks`, `users`, etc.).

4. **Deployment & Documentation**:
   - Deploy the project to Render.com.
   - Ensure the website is live and functional.
   - Write and maintain project documentation (README, code comments).

---

## API Endpoints & Expectations

1. **GET /tasks**
   - Returns a list of tasks in JSON format.
   - Example response:
     ```json
     [
       {
         "id": 1,
         "name": "Buy groceries",
         "completed": false
       },
       {
         "id": 2,
         "name": "Prepare presentation",
         "completed": true
       }
     ]
     ```

2. **POST /tasks**
   - Adds a new task.
   - Example input:
     ```json
     {
       "name": "New Task"
     }
     ```

3. **PUT /tasks/{id}**
   - Updates an existing task (e.g., marking as complete).
   - Example input:
     ```json
     {
       "completed": true
     }
     ```

4. **DELETE /tasks/{id}**
   - Deletes a task by ID.

---

## Hints & Tricks

- **Version control**: Frequently push changes to GitHub for team collaboration.
- **Modular design**: Split large tasks into smaller functions and components for easier debugging and reuse.
- **Documentation**: Write comments for all major functions and keep your code clean.
- **Testing**: Use tools like Postman to test API routes.
- **Responsive design**: Utilize Bootstrap's grid system to make the site mobile-friendly.
```
