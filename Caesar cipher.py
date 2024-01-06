import requests

def submit_to_cuckoo(file_path):
    with open(file_path, "rb") as sample:
        files = {"file": (file_path, sample)}
        response = requests.post("http://localhost:8090/tasks/create/file", files=files)
        
    task_id = response.json()["task_id"]
    print(f"Submitted {file_path} to Cuckoo. Task ID is {task_id}")

# Usage
submit_to_cuckoo("path_to_your_suspicious_file")