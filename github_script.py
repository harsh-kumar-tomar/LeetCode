import os
import subprocess
from datetime import datetime

# Directory for solutions
solutions_dir = "./LeetCode"



def process_directory(title, base_dir, leetcode=False):
    problems = {}
    for root, _, files in os.walk(base_dir):
        for solution_file in sorted(files):
            if not solution_file.endswith('.py'):
                continue

            file_path = os.path.join(root, solution_file)
            relative_path = os.path.relpath(file_path, '.').replace('\\', '/').replace(' ', '%20')

            # Skip extra concept files
            if not solution_file[0].isalnum():
                continue

            # Extract question number and title from filename (split from the right)
            if '.' not in solution_file:
                continue
            question_number, title_part = solution_file.rsplit('.', 1)
            title = title_part.replace('.py', '').strip()

            # Initialize metadata
            link = None

            # Extract link for LeetCode only
            if leetcode:
                with open(file_path, 'r') as f:
                    for line in f:
                        if line.lower().startswith('link'):
                            link = line.split(':', 1)[1].strip()
                            break

            problems[question_number] = {
                'title': title,
                'path': relative_path,
                'link': link
            }

    # Generate section for this platform
    section = f"\n## {title}\n\n"
    section += "| Question No | Title |\n"
    section += "|-------------|-------|\n"
    for q_num in sorted(problems.keys(), key=lambda x: (str(x))):
        p = problems[q_num]
        if p['link']:
            section += f"| [{q_num}]({p['link']}) | [{p['title']}]({p['path']}) |\n"
        else:
            section += f"| {q_num} | [{p['title']}]({p['path']}) |\n"
    return section, len(problems)


def generate_readme():
    total_solved = 0

    # Static badges section
    badges = """
![Python](https://img.shields.io/badge/Python-3.11-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/harsh-kumar-tomar/LeetCode)
![GitHub repo size](https://img.shields.io/github/repo-size/harsh-kumar-tomar/LeetCode)
![Solved](https://img.shields.io/badge/Solved-{total_solved}-blue)
"""

    readme = "# Problem Solutions\n\n"
    readme += "This repository contains solutions for LeetCode, CSES, and Codeforces problems.\n\n"

    # Build sections
    leetcode, count1 = process_directory("LeetCode Solutions", "LeetCode", leetcode=True)
    cses, count2 = process_directory("CSES Problems", "Cses")
    cf, count3 = process_directory("Codeforces Problems", "CF")

    total_solved = count1 + count2 + count3
    readme += badges.format(total_solved=total_solved) + "\n"
    readme += leetcode + cses + cf

    # Write to README.md
    with open("README.md", "w") as f:
        f.write(readme)

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
