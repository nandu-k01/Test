from flask import Flask, request, render_template
import os

app = Flask(__name__, template_folder='templates')

@app.route('/', defaults={'filename': 'file1.txt'}, methods=['GET'])
@app.route('/<filename>', methods=['GET'])
def display_file(filename):
    start_line = request.args.get('start')
    end_line = request.args.get('end')
    file_path = os.path.join(os.getcwd(), filename)

    encoding = 'UTF-8'
    if filename == 'file4.txt':
        encoding = 'UTF-16'

    try:
        with open(file_path, 'r', encoding=encoding) as file:
            if start_line and end_line:
                lines = file.readlines()[int(start_line)-1:int(end_line)]
            else:
                lines = file.readlines()
            return render_template('file.html', filename=filename, lines=lines)
    except Exception as e:
        return render_template('error.html', error=e)

if __name__ == '__main__':
    app.run(debug=True)
