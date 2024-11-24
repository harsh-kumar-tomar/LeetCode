import os


def generate_readme():
    # Directories for questions and solutions
    questions_dir = './Questions'
    solutions_dir = './Solutions'
    readme_content = """# LeetCode Solutions\n\nThis repository contains solutions for LeetCode problems in multiple 
    programming languages.\n\n"""
    readme_content += ("| Question No | Title                                                        | Solution        "
                       "                       | Difficulty | Space Complexity | Time Complexity |\n")
    readme_content += "|-------------|--------------------------------------------------------------|---------------------------------------|------------|------------------|-----------------|\n"

    questions = {}

    for question_file in sorted(os.listdir(questions_dir)):
        if question_file.endswith('.txt'):
            question_path = os.path.join(questions_dir, question_file)

            # Parse question file
            with open(question_path, 'r') as file:
                lines = file.readlines()
                leetcode_link = "-"
                difficulty = "-"
                space_complexity = "-"
                time_complexity = "-"
                question_number, title = question_file.split('.', 1)  # from file name
                title = title.strip().replace('.txt', '')  # from file name

                # Extract metadata
                for line in lines:
                    if line.lower().startswith('link'):
                        leetcode_link = line.split(':', 1)[1].strip()
                    elif line.lower().startswith('difficulty'):
                        difficulty = line.split(':', 1)[1].strip()
                    elif line.lower().startswith('space complexity'):
                        space_complexity = line.split(':', 1)[1].strip()
                    elif line.lower().startswith('time complexity'):
                        time_complexity = line.split(':', 1)[1].strip()

                # Store information in a dictionary
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
            solution_path = os.path.join(solutions_dir, solution_file)
            question_number, title = solution_file.split('.', 1)  # from file name
            title = title.strip().replace('.py', '') # from file name

            # Match the solution with the question details
            question_info = questions.get(question_number, {
                'title': title,
                'link': '-',
                'difficulty': '-',
                'space_complexity': '-',
                'time_complexity': '-',
            })

            # Add row to the README table
            readme_content += (
                f"| {question_number} "
                f"| [{question_info['title']}]({question_info['link']}) "
                f"| [Python](./Solutions/{solution_file}) "
                f"| {question_info['difficulty']} "
                f"| {question_info['space_complexity']} "
                f"| {question_info['time_complexity']} |\n"
            )

        # Write the README file

    with open("README.md", "w") as f:
        f.write(readme_content)

    print("README.md generated successfully.")


if __name__ == "__main__":
    generate_readme()
