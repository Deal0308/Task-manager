from flask import Flask, request
from app.database import task

app = Flask(__name__)   # Flask app instance

@app.get('/tasks')      # http://
def get_all_tasks():
    task_list = task.scan()
    out = {
        "ok": True,
        "tasks": task_list
    }
    return out

@app.get("/tasks/<int:pk>")   
def get_task_by_id(pk):
    single_task = task.select_by_id(pk)
    out = {
        "ok": True,
        "task": single_task
    }
    if not single_task:
        out["message"] = f"Task with id {pk} not found"
    return out

@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    out = {
        "ok": True,
        "message": "Task created successfully"
    }
    return out, 201

@app.put("/tasks/<int:pk>")
def update_task(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "",204

@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete_by_id(pk)
    return "",204