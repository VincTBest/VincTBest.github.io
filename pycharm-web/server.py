from flask import Flask, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/run', methods=['POST'])
def run_code():
    data = request.json
    code = data.get('code')

    try:
        result = subprocess.run(
            ['python', '-c', code],
            text=True,
            capture_output=True,
            timeout=10
        )
        output = result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        output = 'Code execution timed out.'

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(port=5000)
