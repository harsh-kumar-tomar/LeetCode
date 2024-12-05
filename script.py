import os
import subprocess
from datetime import datetime

# Directories for questions and solutions
questions_dir = "./Questions"
solutions_dir = "./Solutions"

def generate_readme():
    # Initialize counters for progress tracker
    total_solved = 0
    difficulty_count = {"Easy": 0, "Medium": 0, "Hard": 0}

    # Start building README content
    badges = """
![Solved](https://img.shields.io/badge/Solved-{total_solved}-blue)
![Easy](https://img.shields.io/badge/Easy-{easy_count}-green)
![Medium](https://img.shields.io/badge/Medium-{medium_count}-orange)
![Hard](https://img.shields.io/badge/Hard-{hard_count}-red)
"""
    readme_content = f"""# LeetCode Solutions

This repository contains solutions for LeetCode problems and additional coding concepts.

{badges}

| Question No | Title | Solution | Difficulty | Space Complexity | Time Complexity |
|-------------|-------|----------|------------|------------------|-----------------|
"""

    # Track questions and solutions
    questions = {}
    solved_files = set()

    # Traverse the Questions folder
    for question_file in sorted(os.listdir(questions_dir)):
        if question_file.endswith('.txt'):
            question_path = os.path.join(questions_dir, question_file)
            with open(question_path, 'r') as file:
                # Parse metadata from the question file
                lines = file.readlines()
                question_number, title = question_file.split('.', 1)
                title = title.strip().replace('.txt', '')

                # Default values
                leetcode_link = difficulty = space_complexity = time_complexity = '-'

                for line in lines:
                    if line.lower().startswith('link'):
                        leetcode_link = line.split(':', 1)[1].strip()
                    elif line.lower().startswith('difficulty'):
                        difficulty = line.split(':', 1)[1].strip()
                        # Count difficulties for progress tracker
                        if difficulty in difficulty_count:
                            difficulty_count[difficulty] += 1
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
                }

    # Traverse the Solutions folder
    concepts_files = []
    for solution_file in sorted(os.listdir(solutions_dir)):
        if solution_file.endswith('.py'):
            question_number, title = solution_file.split('.', 1)
            title = title.strip().replace('.py', '')

            if question_number in questions:
                question_info = questions[question_number]
                # Add row to the Markdown table
                readme_content += f"| {question_number} | [{question_info['title']}]({question_info['link']}) | [Python](./Solutions/{solution_file.replace(' ', '%20')}) | {question_info['difficulty']} | {question_info['space_complexity']} | {question_info['time_complexity']} |\n"
                total_solved += 1
                solved_files.add(solution_file)
            else:
                # File does not correspond to a question
                concepts_files.append(solution_file)

    # Add progress section
    readme_content = readme_content.format(
        total_solved=total_solved,
        easy_count=difficulty_count['Easy'],
        medium_count=difficulty_count['Medium'],
        hard_count=difficulty_count['Hard']
    )

    # Add Concepts Table
    if concepts_files:
        readme_content += "\n## Additional Concepts\n\n"
        readme_content += "| File Name | Description |\n"
        readme_content += "|-----------|-------------|\n"
        for file in concepts_files:
            readme_content += f"| [Python](./Solutions/{file.replace(' ', '%20')}) | To be described |\n"

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
