# bookmark-checker
Certainly! Below is an example of a README.md file for the script that opens a Google Chrome bookmarks file, reads it, visits each bookmark, converts the content to text using BeautifulSoup, and saves the text content in a JSON file.


# Google Chrome Bookmarks Content Extractor

This Python script extracts the text content from the web pages of your Google Chrome bookmarks and saves it in a JSON file. It uses the BeautifulSoup library for web scraping and requests library for making HTTP requests to the bookmarked URLs.

## Requirements

- Python 3.x
- Beautiful Soup 4 (bs4) library
- Requests library

## Installation

1. Install Python 3.x: If you don't have Python 3.x installed, download and install it from the official Python website: https://www.python.org/downloads/

2. Install the required libraries:
   ```bash
   pip install beautifulsoup4 requests
   ```

## How to Use

1. Export Chrome Bookmarks:
   - In Google Chrome, open the bookmarks manager (press `Ctrl+Shift+O` or `Cmd+Shift+O` on macOS).
   - Click on the "..." (More actions) menu on the top-right corner of the bookmarks manager.
   - Choose "Export bookmarks" and save the exported HTML file on your computer.

2. Run the Script:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script `extract_bookmarks_content.py`.
   - Run the script with the following command:
     ```bash
     python extract_bookmarks_content.py --bookmarks_file "path/to/your/chrome_bookmarks_file"
     ```
     Replace `"path/to/your/chrome_bookmarks_file"` with the path to the exported Chrome bookmarks HTML file.

3. Output:
   - The script will visit each bookmarked URL and extract its content using Beautiful Soup.
   - The extracted text content along with bookmark details will be saved in a JSON file with today's date in the filename.

## Options

- `--bookmarks_file` (`-b`): Path to the Google Chrome bookmarks file (optional). If not provided, the script will use the default Chrome bookmarks file location.

- `--browser` (`-b`): Specify the browser (options: 'chrome', 'firefox', 'edge', 'opera'). Default: 'chrome'. This option is useful when specifying a custom bookmarks file path for browsers other than Google Chrome.

## Limitations

- The script is designed to extract the text content of the first 10 bookmarks in the bookmark bar for testing purposes. You can modify this limit as per your requirements.

## Contribution

Contributions to this script are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


This README.md file provides an overview of the script, its requirements, installation instructions, usage guidelines, and other relevant details for potential users or contributors. You can customize the README file further to suit the specifics of your project and include additional information if needed.
