import os
import shutil
import re
from categories import Categories
from typing import List

solutions_dir = "./Solutions"

def extract_category(line):
    match = re.search(r'Categories\.(\w+)', line)
    if match:
        category_name = match.group(1)
        return getattr(Categories, category_name, None)
    return None

def organize_solutions():
    for filename in os.listdir(solutions_dir):
        file_path = os.path.join(solutions_dir, filename)

        if filename.endswith(".py"):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            path = None
            for line in lines:
                if "path =" in line:
                    path = extract_category(line)
                    break

            if path:
                target_dir = os.path.join(solutions_dir, path.strip('/'))
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(target_dir, filename))
                print(f"✅ Moved {filename} to {target_dir}")
            else:
                print(f"⚠️ Warning: Invalid or missing path in {filename}. File was NOT moved.")

if __name__ == "__main__":
    organize_solutions()
