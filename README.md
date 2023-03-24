# Test

## Overview
Flask File Viewer is a simple web application that allows you to view the contents of text files in your browser.

## Installation
```bash
# Clone this repository
$ git clone https://github.com/nandu-k01/Test.git
# Go into the repository
$ cd Test
# Install requirements.txt
$ pip install -r requirements.txt
# Run the app
$ python app.py
```
## Usage
1. In your web browser, navigate to http://localhost:5000/<filename> to view the entire file.
2. To view only a specific section of the file, add ?start=<start_line>&end=<end_line> to the URL. For example, http://localhost:5000/file1.txt?start=1&end=10 will display lines 1 through 10 of file1.txt.
