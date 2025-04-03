import requests
from bs4 import BeautifulSoup
import os

url = "https://walkccc.me/LeetCode/problems/31/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Save HTML
    with open("archive.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    # Find and download all CSS files
    css_links = [link["href"] for link in soup.find_all("link", rel="stylesheet") if "href" in link.attrs]

    os.makedirs("css", exist_ok=True)  # Create a folder for CSS files

    for css_url in css_links:
        css_url = css_url if css_url.startswith("http") else url + css_url
        css_response = requests.get(css_url)

        if css_response.status_code == 200:
            css_filename = os.path.join("css", os.path.basename(css_url))
            with open(css_filename, "w", encoding="utf-8") as css_file:
                css_file.write(css_response.text)
            print(f"Saved: {css_filename}")

    print("Website archived successfully.")
else:
    print("Failed to retrieve the website.")
