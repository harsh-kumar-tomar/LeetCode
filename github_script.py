import os
import subprocess
from datetime import datetime

# Directory for solutions
solutions_dir = "./LeetCode"


def generate_readme():
    total_question_solved = 0

    badges = """
![Python](https://img.shields.io/badge/Python-3.11-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/harsh-kumar-tomar/LeetCode)
![GitHub repo size](https://img.shields.io/github/repo-size/harsh-kumar-tomar/LeetCode)

![Solved](https://img.shields.io/badge/Solved-{total_question_solved}-blue)
"""

    readme_content = f"""# LeetCode Solutions

This repository contains solutions for LeetCode problems and additional coding concepts.

{badges}

| Question No | Title |
|-------------|-------|
"""

    questions = {}
    concept_hashmap = {}

    for root, _, files in os.walk(solutions_dir):
        for solution_file in sorted(files):
            if solution_file.endswith('.py'):
                question_path = os.path.join(root, solution_file)
                relative_path = os.path.relpath(question_path, '.')  # relative to repo root
                github_path = relative_path.replace('\\', '/').replace(' ', '%20')  # fix for GitHub

                with open(question_path, 'r') as file:
                    lines = file.readlines()

                if not solution_file[0].isdigit():
                    concept_hashmap[solution_file] = github_path
                    continue

                question_number, title = solution_file.split('.', 1)
                title = title.strip().replace('.py', '')

                leetcode_link = "-"
                for line in lines:
                    if line.lower().startswith('link'):
                        leetcode_link = line.split(':', 1)[1].strip()
                        break

                questions[int(question_number)] = {
                    'title': title,
                    'link': leetcode_link,
                    'path': github_path
                }

    for q_num in sorted(questions.keys()):
        q = questions[q_num]
        readme_content += f"| [{q_num}]({q['link']}) | [{q['title']}]({q['path']}) |\n"
        total_question_solved += 1

    readme_content = readme_content.format(total_question_solved=total_question_solved)

    if concept_hashmap:
        readme_content += "\n## Additional Concepts\n\n"
        readme_content += "| File Name |\n"
        readme_content += "|-----------|\n"
        for file_name, path in concept_hashmap.items():
            readme_content += f"| [{file_name}]({path}) |\n"

    with open("README.md", "w") as f:
        f.write(readme_content)

    print("✅ README.md generated successfully.")    

def git_push():
    # Get today's date in "DD MMM YYYY" format
    today_date = datetime.now().strftime("%d %b %Y")

    # Run Git commands to stage, commit, and push changes
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Update solutions and README on {today_date}"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🚀 Changes pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print("❌ Error while pushing changes to GitHub:", e)


# Run the script
if __name__ == "__main__":
    generate_readme()
    git_push()
