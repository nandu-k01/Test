from flask import Flask, request, render_template
import os

app = Flask(__name__, template_folder='templates')

# creating app and setting defaults
@app.route('/', defaults={'filename': 'file1.txt'}, methods=['GET'])
# url to accept file name
@app.route('/<filename>', methods=['GET'])
def display_file(filename):
    start_line = request.args.get('start')
    end_line = request.args.get('end')
    file_path = os.path.join(os.getcwd(), filename)

# encoding set to utf-8 for first 3 files and utf-16 for file4 as it contains chinese
    encoding = 'UTF-8'
    if filename == 'file4.txt':
        encoding = 'UTF-16'

# reading txt files
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            if start_line and end_line:
                lines = file.readlines()[int(start_line)-1:int(end_line)]
            else:
                lines = file.readlines()
            return render_template('file.html', filename=filename, lines=lines)

# error handling        
    except FileNotFoundError:
        error_msg = f"The file '{filename}' does not exist."
        return render_template('error.html', error=error_msg)
    except Exception as e:
        return render_template('error.html', error=e)

if __name__ == '__main__':
    app.run(debug=True)
