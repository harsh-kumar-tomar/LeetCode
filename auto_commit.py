import subprocess
from datetime import datetime

# Directory of the Git repository (adjust the path if necessary)
repo_dir = r"C:\Users\Harsh Ji\Desktop\LeetCode"

# Get the current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"Auto-commit on {current_time}"

try:
    # Change the working directory to the repo directory
    subprocess.run(["git", "-C", repo_dir, "add", "."], check=True)
    subprocess.run(["git", "-C", repo_dir, "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "-C", repo_dir, "push", "origin", "main"], check=True)
    print(f"Commit and push successful: {commit_message}")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
