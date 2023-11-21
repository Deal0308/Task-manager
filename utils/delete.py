import requests

def delete_task(task_id):
    # Assuming the API endpoint for deleting tasks is at the following URL
    delete_url = f"http://127.0.0.1:5000/tasks/{task_id}"

    # Fetch the existing task data
    response = requests.get(delete_url)
    existing_task = response.json()

    # Display the existing task
    print("Existing Task:")
    print(existing_task)

    # Prompt user for confirmation
    confirm_deletion = input("Do you want to delete this task? (yes/no): ").lower()

    if confirm_deletion == "yes":
        # Send a DELETE request to delete the task
        response = requests.delete(delete_url)

        if response.status_code == 204:
            print("Task deleted successfully.")
        else:
            print(f"Failed to delete task. Status Code: {response.status_code}")
            print(response.text)
    else:
        print("Task deletion canceled.")

# Prompt the user for a task id to delete
task_id_to_delete = input("Enter the task ID to delete: ")
delete_task(task_id_to_delete)
