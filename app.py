from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    file_name = request.args.get('n')
    line_number = request.args.get('m')

    if file_name is None:
        return "Missing 'n' parameter", 400

    file_path = f'/tmp/data/{file_name}.txt'

    if line_number is None:
        # Return entire file content if only 'n' is provided
        with open(file_path, 'r') as file:
            return file.read()
    else:
        # Return specific line content if both 'n' and 'm' are provided
        try:
            line_number = int(line_number)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                return lines[line_number - 1]
        except FileNotFoundError:
            return "File not found", 404
        except ValueError:
            return "Invalid 'm' parameter", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
