import requests


def update_task(task_id, summary, description, is_done):
    update_url = f"http://127.0.0.1:5000/tasks/{task_id}"

    # Fetch the existing task data
    response = requests.get(update_url)
    existing_task = response.json()

    # Display the existing task
    print("Existing Task:")
    print(existing_task)

    # Prompt user for updated values
    summary = input("Enter updated summary: ") or existing_task.get("summary", "")
    description = input("Enter updated description: ") or existing_task.get("description", "")
    is_done = input("Is the task done? (True/False): ").capitalize() or existing_task.get("is_done", False)

    # Update the task with new values
    updated_task = {
        "summary": summary,
        "description": description,
        "is_done": is_done
    }

    # Send a PUT request to update the task
    response = requests.put(update_url, json=updated_task)

    if response.status_code == 200:
        print("Task updated successfully.")
    else:
        print(f"Failed to update task. Status Code: {response.status_code}")
        print(response.text)

# Prompt the user for a task id to update
task_id_to_update = input("Enter the task ID to update: ")
update_task(task_id_to_update, "", "", "")
