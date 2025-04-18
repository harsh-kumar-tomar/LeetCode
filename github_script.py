import os
import subprocess
from datetime import datetime


# Directory for solutions
solutions_dir = "."
cf_dir = "./CF"
cses_dir = "./Cses"
leetcode_dir = "./LeetCode"
total_problems_solved = 0

leetcode_read_me = "# LeetCode\n"
cf_read_me = "# Codeforces\n"
cses_read_me = "# Cses\n"
final_read_me = ""


def handle_leetcode(files:list[str]):
    print("Leetcode")
    global leetcode_read_me
    leetcode_read_me += "|Problem|Question|\n"
    leetcode_read_me += "|-|-|\n"

    for file in files:
        numeric , title = file.split('.',maxsplit=1)

        file_path = f"{leetcode_dir}/{file}"
        leetcode_web_link = get_link_from_file(file_path)

        leetcode_read_me += f"|[{numeric}]({leetcode_web_link}) | [{title.removesuffix(".py")}]({file_path.replace(' ','%20')})|\n"
        
    print(leetcode_read_me)
        
def get_link_from_file(file_path:str):
    link = ""
    with open(os.path.normpath(file_path),'r') as f:
        for line in f:
            if line.startswith("link") or line.startswith("Link"):
                link = "https" + line.split("https")[1]
    
    return link.strip()

def handle_cf(files:list[str]):
    print("cf")
    global cf_read_me
    cf_read_me += "|Problem|Question|\n"
    cf_read_me += "|-|-|\n"
    # 110A. Nearly Lucky Number.py
    for file in files:
        alpha_numeric , title = file.split('.',maxsplit=1)
        contest_num , alphabet = alpha_numeric[:len(alpha_numeric)-2:] , alpha_numeric[-1]
        
        file_path = f"{cf_dir}/{file}" 
        
        cf_web_link = "https://codeforces.com/problemset/problem/{}/{}".format(contest_num,alphabet)

        cf_read_me += f"|[{alpha_numeric}]({cf_web_link}) | [{title.removesuffix(".py")}]({file_path.replace(' ','%20')})|\n"

def handle_cses(subfolder_name:str,files:list[str]):

    if len(files) == 0 :
        return
    global cses_read_me

    cses_read_me += f"## {subfolder_name}\n" 
    cses_read_me += "|Question/Solutions|\n"
    cses_read_me += "|-|\n"
    for file in files:
        title = file
        file_path = f"{cses_dir}/{subfolder_name}/{file}"
        
        cses_read_me += f"|[{title.removesuffix('.py')}]({file_path.replace(' ','%20')})|\n"

    print(cses_read_me)



for root, _, files in os.walk(solutions_dir):

    folder_name = os.path.normpath(root).split('\\')
    # print(folder_name,len(files))
    if folder_name[0] == "LeetCode":
        handle_leetcode(files)
    elif folder_name[0] == "Cses" and len(folder_name) > 1 :
        handle_cses(folder_name[1],files)
    elif folder_name[0] == "CF":
        handle_cf(files)

with open("README.md", "w") as f:
        f.write(leetcode_read_me + "\n" + cf_read_me + "\n" + cses_read_me)

print("✅ README.md generated successfully.")



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


