import os
import subprocess
from datetime import datetime


# Directory for solutions
solutions_dir = "."
cf_dir = "./CF"
cses_dir = "./Cses"
leetcode_dir = "./LeetCode"
atcoder_dir = "./AtCoder"


total_problems_solved = 0
count_leetcode = 0
count_cf = 0
count_cses = 0
count_atcoder = 0

leetcode_profile_link = "https://leetcode.com/u/GhostInPixels/"
cf_profile_link = "https://codeforces.com/profile/harshkumartomar"
cses_profile_link = "https://cses.fi/user/321162"

base_read_me = """
![GitHub last commit](https://img.shields.io/github/last-commit/harsh-kumar-tomar/LeetCode)
![GitHub repo size](https://img.shields.io/github/repo-size/harsh-kumar-tomar/LeetCode)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)
"""

leetcode_read_me = "# LeetCode\n"
cf_read_me = "# Codeforces\n"
cses_read_me = "# Cses\n"
atcoder_read_me = "# AtCoder\n"
final_read_me = ""


def get_count_badge(title:str,count:int,color:str = "blue",link = None):
    badge = "![{}](https://img.shields.io/badge/{}-{}-{})".format(title,title,count,color)
    if link :
        return f"[{badge}]({link})\n"
    else:
        return f"{badge}\n"

def sort_leetcode_files(files:list[str]):
    file_map = {}
    # 1. Two Sum.py
    for file in files:
        numeric , title = file.split('.',maxsplit=1)
        if numeric.isnumeric():
            file_map[int(numeric)] = "."+title
    
    sorted_file_map = dict(sorted(file_map.items())) 
    sorted_files_list = []

    for key,val in sorted_file_map.items():
        sorted_files_list.append(str(key)+val)
    
    return sorted_files_list
    
def handle_leetcode(files:list[str]):
    global leetcode_read_me,total_problems_solved,count_leetcode

    files = sort_leetcode_files(files)

    total_problems_solved += len(files)
    count_leetcode = len(files)


    leetcode_read_me += "|Problem|Question|\n"
    leetcode_read_me += "|-|-|\n"

    for file in files:
        numeric , title = file.split('.',maxsplit=1)

        file_path = f"{leetcode_dir}/{file}"
        leetcode_web_link = get_link_from_file(file_path)

        leetcode_read_me += f"|[{numeric}]({leetcode_web_link}) | [{title.removesuffix(".py")}]({file_path.replace(' ','%20')})|\n"
        
def get_link_from_file(file_path:str):
    link = ""
    with open(os.path.normpath(file_path),'r') as f:
        for line in f:
            if line.startswith("link") or line.startswith("Link"):
                link = "https" + line.split("https")[1]
    
    return link.strip()

def split_cf_alphanumeric(alphanumeric:str):
    index = -1
    for i,char in enumerate(alphanumeric):
        if char.isalpha():
            index = i
    
    return (alphanumeric[:index],alphanumeric[index:])

def handle_cf(files:list[str]):

    global cf_read_me , total_problems_solved , count_cf

    total_problems_solved += len(files)
    count_cf = len(files)

    cf_read_me += "|Problem|Question|\n"
    cf_read_me += "|-|-|\n"

    for file in files:
        alpha_numeric , title = file.split('.',maxsplit=1)
        contest_num , alphabet = split_cf_alphanumeric(alpha_numeric)
        
        file_path = f"{cf_dir}/{file}" 
        
        cf_web_link = "https://codeforces.com/problemset/problem/{}/{}".format(contest_num,alphabet)

        cf_read_me += f"|[{alpha_numeric}]({cf_web_link}) | [{title.removesuffix(".py")}]({file_path.replace(' ','%20')})|\n"

def handle_cses(subfolder_name:str,files:list[str]):

    if len(files) == 0 :
        return
    
    global cses_read_me,total_problems_solved,count_cses

    count_cses += len(files)
    total_problems_solved += len(files)

    cses_read_me += f"## {subfolder_name}\n" 
    cses_read_me += "|Question/Solutions|\n"
    cses_read_me += "|-|\n"
    for file in files:
        title = file
        file_path = f"{cses_dir}/{subfolder_name}/{file}"
        
        cses_read_me += f"|[{title.removesuffix('.py')}]({file_path.replace(' ','%20')})|\n"

def handle_atcoder(subfolder_name:str,files:list[str]):
    if len(files) == 0:
        return
    
    global count_atcoder , total_problems_solved , atcoder_read_me

    count_atcoder += len(files)
    total_problems_solved += count_atcoder
    atcoder_read_me += f"## {subfolder_name} Contest\n"
    atcoder_read_me += "|Contest|Question|\n"
    atcoder_read_me += "|-|-|\n"

    for file in files:
        file_path = f"{atcoder_dir}/{subfolder_name}/{file}"
        numeric , title = [part.strip() for part in file.split("-")]

        contest_name_num = f"{subfolder_name}{numeric[:len(numeric)-1].lower()}"
        atcoder_web_link = "https://atcoder.jp/contests/{}/tasks/{}_{}".format(contest_name_num,contest_name_num,numeric[-1].lower())
        atcoder_read_me += f"|[{numeric}]({atcoder_web_link}) | [{title.removesuffix(".py")}]({file_path.replace(' ','%20')})|\n"



def get_base_read_me():
    global base_read_me
    base_read_me += get_count_badge("Solved",total_problems_solved) + get_count_badge("LeetCode",count_leetcode,"FFA116",leetcode_profile_link) + get_count_badge("CF",count_cf,"1F8ACB",cf_profile_link) + get_count_badge("Cses",count_cses,"5E5E5E",cses_profile_link) + get_count_badge("AtCoder",count_atcoder,"0080ff")
    return base_read_me

for root, _, files in os.walk(solutions_dir):

    folder_name = os.path.normpath(root).split('\\')

    if folder_name[0] == "LeetCode":
        handle_leetcode(files)
    elif folder_name[0] == "Cses" and len(folder_name) > 1 :
        handle_cses(folder_name[1],files)
    elif folder_name[0] == "AtCoder" and len(folder_name) > 1 :
        handle_atcoder(folder_name[1],files)
    elif folder_name[0] == "CF":
        handle_cf(files)

with open("README.md", "w") as f:
        f.write( get_base_read_me() + leetcode_read_me + "\n" + cf_read_me + "\n" + cses_read_me + "\n" + atcoder_read_me)

print("✅ README.md generated successfully.")



today_date = datetime.now().strftime("%d %b %Y")

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"Update solutions and README on {today_date}"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("🚀 Changes pushed to GitHub successfully.")
except subprocess.CalledProcessError as e:
    print("❌ Error while pushing changes to GitHub:", e)


