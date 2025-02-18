import os
import subprocess
from datetime import datetime

# Directory for solutions
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

This repository contains solutions for LeetCode problems and additional coding concepts.

{badges}

| Question No | Title | Solution | Difficulty | Space Complexity | Time Complexity |
|-------------|-------|----------|------------|------------------|-----------------|
"""

    # Track questions and solutions
    questions = {}
    concept_hashmap = {}

    # Traverse the Solutions folder (including subdirectories)
    for root, _, files in os.walk(solutions_dir):
        for solution_file in sorted(files):
            if solution_file.endswith('.py'):
                question_path = os.path.join(root, solution_file)
                relative_path = os.path.relpath(question_path, solutions_dir)  # Get path relative to Solutions/
                with open(question_path, 'r') as file:
                    lines = file.readlines()

                # Identify additional concepts by checking file name pattern
                if not solution_file[0].isdigit():
                    concept_hashmap[solution_file] = relative_path
                    continue

                question_number, title = solution_file.split('.', 1)
                title = title.strip().replace('.py', '')

                # Default values
                leetcode_link = difficulty = space_complexity = time_complexity = '-'

                for line in lines:
                    if line.lower().startswith('link'):
                        leetcode_link = line.split(':', 1)[1].strip()
                    elif line.lower().startswith('difficulty'):
                        difficulty = line.split(':', 1)[1].strip()
                        if difficulty in difficulty_count_hash_map:
                            difficulty_count_hash_map[difficulty] += 1
                    elif line.lower().startswith('space complexity'):
                        space_complexity = line.split(':', 1)[1].strip()
                    elif line.lower().startswith('time complexity'):
                        time_complexity = line.split(':', 1)[1].strip()

                # Store question metadata
                questions[question_number] = {
                    'title': title,
                    'link': leetcode_link,
                    'difficulty': difficulty,
                    'space_complexity': space_complexity,
                    'time_complexity': time_complexity,
                    'path': relative_path.replace(' ', '%20')  # Format for GitHub links
                }

    # Add questions to the README
    for question_info in sorted(questions.keys(), key=lambda x: int(x)):  # Sort by question number
        question = questions[question_info]
        readme_content += f"| {question_info} | [{question['title']}]({question['link']}) | [Python](./Solutions/{question['path']}) | {question['difficulty']} | {question['space_complexity']} | {question['time_complexity']} |\n"
        total_question_solved += 1

    # Progress section
    readme_content = readme_content.format(
        total_question_solved=total_question_solved,
        easy_count=difficulty_count_hash_map['Easy'],
        medium_count=difficulty_count_hash_map['Medium'],
        hard_count=difficulty_count_hash_map['Hard']
    )

    # Additional Concepts Table
    if concept_hashmap:
        readme_content += "\n## Additional Concepts\n\n"
        readme_content += "| File Name |\n"
        readme_content += "|-----------|\n"
        for file_name, path in concept_hashmap.items():
            file_link = f"./Solutions/{path.replace(' ', '%20')}"
            readme_content += f"| [{file_name}]({file_link}) |\n"

    # Write the README file
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
