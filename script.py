import os

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

This repository contains solutions for LeetCode problems in multiple programming languages.

{badges}

| Question No | Title | Solution | Difficulty | Space Complexity | Time Complexity |
|-------------|-------|----------|------------|------------------|-----------------|
"""

    # Traverse the Questions folder
    questions = {}
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
    for solution_file in sorted(os.listdir(solutions_dir)):
        if solution_file.endswith('.py'):
            question_number, title = solution_file.split('.', 1)
            title = title.strip().replace('.py', '')

            question_info = questions.get(question_number, {
                'title': title,
                'link': '-',
                'difficulty': '-',
                'space_complexity': '-',
                'time_complexity': '-',
            })

            # Add row to the Markdown table
            readme_content += f"| {question_number} | [{question_info['title']}]({question_info['link']}) | [Python](./Solutions/{solution_file.replace(' ', '%20')}) | {question_info['difficulty']} | {question_info['space_complexity']} | {question_info['time_complexity']} |\n"
            total_solved += 1

    # Add progress section
    readme_content = readme_content.format(
        total_solved=total_solved,
        easy_count=difficulty_count['Easy'],
        medium_count=difficulty_count['Medium'],
        hard_count=difficulty_count['Hard']
    )

    # Write the README file
    with open("README.md", "w") as f:
        f.write(readme_content)

    print("README.md generated successfully.")

# Run the script
if __name__ == "__main__":
    generate_readme()
