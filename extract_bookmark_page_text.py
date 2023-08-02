import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import random
from urllib.parse import urlparse
import argparse

def get_bookmark_text(url):
    # Fetches the text content of the bookmarked URL using Beautiful Soup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def get_default_bookmarks_file_path(browser):
    # Returns the default bookmarks file path based on the specified browser
    if browser == "chrome":
        return os.path.expanduser('~') + '/AppData/Local/Google/Chrome/User Data/Default/Bookmarks'
    elif browser == "firefox":
        return os.path.expanduser('~') + '/AppData/Roaming/Mozilla/Firefox/Profiles/default/places.sqlite'
    elif browser == "edge":
        return os.path.expanduser('~') + '/AppData/Local/Microsoft/Edge/User Data/Default/Bookmarks'
    elif browser == "opera":
        return os.path.expanduser('~') + '/AppData/Roaming/Opera Software/Opera Stable/Bookmarks'
    else:
        raise ValueError("Invalid browser option. Supported options: 'chrome', 'firefox', 'edge', 'opera'.")

def main(bookmarks_file_path, browser):
    # If browser is not provided, set it to "chrome" (default)
    if not browser:
        browser = "chrome"

    # Load bookmarks data from the specified file or use the default bookmarks file path
    if bookmarks_file_path:
        file_path = bookmarks_file_path
    else:
        file_path = get_default_bookmarks_file_path(browser)

    # Check if the file exists before proceeding
    if not os.path.exists(file_path):
        print(f"Error: The bookmarks file '{file_path}' was not found.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            bookmarks_data = json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error: Failed to read the bookmarks file: {e}")
        return

    bookmarks = []
    count = 0

    for bookmark in bookmarks_data['roots']['bookmark_bar']['children']:
        if count >= 10:  # Limit to the first 10 entries for testing
            break

        if 'url' in bookmark:
            url = bookmark['url']
            created_datetime = bookmark['date_added']

            try:
                text_content = get_bookmark_text(url)
            except requests.exceptions.RequestException:
                text_content = "Failed to fetch content."

            current_date = datetime.now().isoformat()

            # Extract the domain from the URL for console output
            domain = urlparse(url).netloc
            print(f"Processing bookmark: {domain}")

            bookmarks.append({
                'url': url,
                'created_datetime': created_datetime,
                'text_content': text_content,
                'current_date': current_date
            })

            count += 1

            # Pause with a random duration between 3 to 10 seconds
            pause_duration = random.randint(3, 10)
            time.sleep(pause_duration)

    # Save the results to a JSON file with today's datetime in the filename
    today_date = datetime.now().strftime("%Y-%m-%d")
    output_file = f'bookmarks_content_{browser}_{today_date}.json'
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(bookmarks, outfile, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    # Handle command-line arguments
    parser = argparse.ArgumentParser(description="Process browser bookmarks and save text content.")
    parser.add_argument('--bookmarks_file', '-b', help="Path to the browser bookmarks file.")
    parser.add_argument('--browser', choices=['chrome', 'firefox', 'edge', 'opera'], default='chrome',
                        help="Specify the browser (options: 'chrome', 'firefox', 'edge', 'opera'). Default: 'chrome'.")
    args = parser.parse_args()

    main(args.bookmarks_file, args.browser)
