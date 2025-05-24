import os
import requests
import time
import threading


def format_chapter_number(chapter_num):
    """Format chapter number to ensure four-digit padding before the decimal."""
    if isinstance(chapter_num, float):
        whole, decimal = str(chapter_num).split(".")
        return f"{int(whole):04d}.{decimal}"  # e.g., 223.9 → "0223.9"
    return f"{chapter_num:04d}"  # e.g., 71 → "0071"


def download_chapter(manga, chapter_num, root_dir):
    """Download a specific chapter of the manga, using correct URL formatting."""

    chapter_str = format_chapter_number(chapter_num)  # Ensure correct format
    chapter_dir = os.path.join(root_dir, f"Chapter_{chapter_str}")
    os.makedirs(chapter_dir, exist_ok=True)

    page_num = 1  # Start from page 001
    found_page = False  # Flag to check if chapter has pages

    while True:  # Loop through pages
        image_url = f"https://official.lowee.us/manga/{manga}/{chapter_str}-{page_num:03d}.png"
        # image_url = f"https://scans.lastation.us/manga/{manga}/{chapter_str}-{page_num:03d}.png"
        image_path = os.path.join(chapter_dir, f"page_{page_num:03d}.png")

        try:
            response = requests.get(image_url, stream=True, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            })
            if response.status_code == 200:
                with open(image_path, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"Downloaded: {image_path}")
                found_page = True  # At least one page was found
            else:
                break  # No more pages in this chapter
        except Exception as e:
            print(f"Error downloading {image_url}: {e}")
            break

        page_num += 1  # Move to next page
        # time.sleep(1)  # Add a delay to prevent rate-limiting

    return found_page  # Return whether the chapter had pages


def download_manga(manga, start_chapter=1, list_chapter=None):
    """Download manga chapters sequentially and from a specific list if provided."""

    root_dir = manga.replace(" ", "-")  # Ensure safe folder name
    os.makedirs(root_dir, exist_ok=True)

    if start_chapter != -1:
        chapter_num = start_chapter
        while download_chapter(manga, chapter_num, root_dir):
            chapter_num += 1  # Move to next whole number chapter

    if list_chapter:
        for chapter in list_chapter:
            download_chapter(manga, chapter, root_dir)

    print(f"Download complete for {manga}!")


def download_multiple_manga(manga_list):
    """Run multiple manga downloads in parallel using threads."""

    threads = []

    for manga, start_chapter, list_chapter in manga_list:
        # thread = threading.Thread(target=download_manga, args=(manga, start_chapter, list_chapter))
        download_manga(manga,start_chapter,list_chapter)
        # threads.append(thread)
        # thread.start()

    # for thread in threads:
    #     thread.join()

    print("All manga downloads complete!")


# Example usage:
download_multiple_manga([
    ("Koe-No-Katachi", 37, []),  # Downloads 108.1, 108.2, etc.
    # ("One-Punch-Man", -1, [5, 12.1, 223.9])  # Only downloads 5, 12.1, and 223.9
])
