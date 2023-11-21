import requests
import requests
import requests

BACKEND_URL = "http://127.0.0.1:5000/tasks"

def create_task(summary, description):
    raw_task = {
        "summary": summary,
        "description": description
    }
    response = requests.post(BACKEND_URL, json=raw_task)
    if response.status_code == 201:
        print("Task created successfully")
    else:
        print("Something went wrong")

if __name__ == "__main__":
    print("Create a task by following the prompt below:")
    summary = input("Summary: ")
    description = input("Description: ")
    create_task(summary, description)