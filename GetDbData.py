
import os
import re

solutions_dir = "./Solutions"

def extract_solution(file_path):
    """Extracts structured data from a solution file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract fields using regex
    data = {
        "link": re.search(r"Link:\s*(.+)", content),
        "difficulty": re.search(r"Difficulty:\s*(.+)", content),
        "space_complexity": re.search(r"Space Complexity:\s*(.+)", content),
        "time_complexity": re.search(r"Time Complexity:\s*(.+)", content),
        "description": re.search(r"Description:\s*(.+)", content, re.DOTALL),
        "approaches": re.findall(r"Approach \d+:(.*?)Code:", content, re.DOTALL),
        "code": re.search(r"```python(.*?)```", content, re.DOTALL)
    }

    # Clean up extracted data
    for key in data:
        if isinstance(data[key], list):  # Multiple approaches
            data[key] = [x.strip() for x in data[key]]
        elif data[key]:  # Single match
            data[key] = data[key].group(1).strip()
        else:
            data[key] = None  # If field not found

    return data

solution_data = extract_solution(solutions_dir)
print(solution_data)
