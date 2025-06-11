import requests
import subprocess
import os
import shutil
import json

OUTPUT_DIR = "cf_archive"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"

def get_all_problems():
    url = "https://codeforces.com/api/problemset.problems"
    print("Fetching problems from Codeforces API...")
    res = requests.get(url)
    data = res.json()
    problems = data['result']['problems']
    return [(str(p['contestId']), p['index']) for p in problems if 'contestId' in p and 'index' in p]

def download_problem(contest_id, problem_index):
    problem_name = f"{contest_id}{problem_index}"
    url = f"https://codeforces.com/problemset/problem/{contest_id}/{problem_index}"

    temp_dir = os.path.join(OUTPUT_DIR, "__temp")
    os.makedirs(temp_dir, exist_ok=True)

    wget_cmd = [
        "wget",
        "--wait=2",
        "--random-wait",
        "--convert-links",
        "--page-requisites",
        "--no-parent",
        "--directory-prefix", temp_dir,
        "--user-agent", USER_AGENT,
        url
    ]

    print(f"📥 Downloading {problem_name} ...")
    result = subprocess.run(wget_cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ Failed: {problem_name}\n{result.stderr}")
        return

    # Locate the HTML file
    # subfolder = os.path.join(temp_dir, "codeforces.com", "problemset", "problem", contest_id, problem_index)
    # if not os.path.exists(subfolder):
    #     print(f"⚠️ Page structure not found for {problem_name}")
    #     return

    # html_path = os.path.join(subfolder, "index.html")
    # if not os.path.exists(html_path):
    #     print(f"⚠️ index.html missing for {problem_name}")
    #     return

    # # Move and rename
    # final_path = os.path.join(OUTPUT_DIR, f"{problem_name}.html")
    # os.makedirs(OUTPUT_DIR, exist_ok=True)
    # shutil.move(html_path, final_path)
    # print(f"✅ Saved as: {final_path}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    problems = get_all_problems()
    
    for contest_id, index in problems:
        download_problem(contest_id, index)

    # Clean up temp directory
    shutil.rmtree(os.path.join(OUTPUT_DIR, "__temp"), ignore_errors=True)

if __name__ == "__main__":
    main()
