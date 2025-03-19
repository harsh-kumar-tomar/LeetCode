import requests

url = "https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/"
response = requests.get(url)

if response.status_code == 200:
    with open("archive.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Website archived successfully.")
else:
    print("Failed to retrieve the website.")
