import os
import subprocess
from datetime import datetime

# Directories for questions and solutions
solutions_dir = "./Solutions"


def generate_readme():
    # Initialize counters for progress tracker
    total_question_solved = 0
    difficulty_count_hash_map = {"Easy": 0, "Medium": 0, "Hard": 0}

    # Start building README content
    badges = """
![Solved](https://img.shields.io/badge/Solved-{total_question_solved}-blue)
![Easy](https://img.shields.io/badge/Easy-{easy_count}-green)
![Medium](https://img.shields.io/badge/Medium-{medium_count}-orange)
![Hard](https://img.shields.io/badge/Hard-{hard_count}-red)
"""
    readme_content = f"""# LeetCode Solutions

This repository contains soltions for LeetCode problems and additional coding concepts.

{badges}

| Question No | Title | Solution | Difficulty | Space Complexity | Time Complexity |
|-------------|-------|----------|------------|------------------|-----------------|
"""

    # Track questions and solutions
    questions = {}
    concept_hashmap = {}

    # Traverse the Questions folder
    for solution_file in sorted(os.listdir(solutions_dir)):
        if solution_file.endswith('.py'):
            question_path = os.path.join(solutions_dir, solution_file)
            with open(question_path, 'r') as file:
                # Parse metadata from the question file
                lines = file.readlines()

                if '.' not in solution_file:
                    concept_hashmap[solution_file] = solution_file
                    continue
                else:
                    question_number, title = solution_file.split('.', 1)
                    title = title.strip().replace('.py', '')

                # Default values
                leetcode_link = difficulty = space_complexity = time_complexity = '-'

                for line in lines:
                    if line.lower().startswith('link'):
                        leetcode_link = line.split(':', 1)[1].strip()
                    elif line.lower().startswith('difficulty'):
                        difficulty = line.split(':', 1)[1].strip()
                        # Count difficulties for progress tracker
                        if difficulty in difficulty_count_hash_map:
                            difficulty_count_hash_map[difficulty] += 1
                    elif line.lower().startswith('space complexity'):
                        space_complexity = line.split(':', 1)[1].strip()
                    elif line.lower().startswith('time complexity'):
                        time_complexity = line.split(':', 1)[1].strip()

                # Store information
                questions[question_number] = {
                    'title': title,
                    'link': leetcode_link,
                    'difficulty': difficulty,
                    'space_complexity': space_complexity,
                    'time_complexity': time_complexity,
                    'path': solution_file.replace(' ', '%20')
                }

    # Traverse the Solutions folder
    concepts_files = []

    for question_info in questions:
        # Add row to the Markdown table
        question = questions[question_info]
        readme_content += f"| {question_info} | [{question['title']}]({question['link']}) | [Python](./Solutions/{question['path']}) | {question['difficulty']} | {question['space_complexity']} | {question['time_complexity']} |\n"
        total_question_solved += 1

    # progress section
    readme_content = readme_content.format(
        total_question_solved=total_question_solved,
        easy_count=difficulty_count_hash_map['Easy'],
        medium_count=difficulty_count_hash_map['Medium'],
        hard_count=difficulty_count_hash_map['Hard']
    )

    # Concepts Table
    readme_content += "\n## Additional Concepts\n\n"
    readme_content += "| File Name |\n"
    readme_content += "|-----------|\n"
    for file_name, path in concept_hashmap.items():
        # Remove .py extension and link to the file
        file_link = f"./Solutions/{path.replace(' ', '%20')}"
        readme_content += f"| [{file_name}]({file_link}) |\n"


    # Write the README file
    with open("README.md", "w") as f:
        f.write(readme_content)

    print("README.md generated successfully.")


def git_push():
    # Get today's date in "DD MMM YYYY" format
    today_date = datetime.now().strftime("%d %b %Y")

    # Run Git commands to stage, commit, and push changes
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Update solutions and README on {today_date}"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Changes pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print("Error while pushing changes to GitHub:", e)


# Run the script
if __name__ == "__main__":
    generate_readme()
    git_push()
