from flask import Flask, send_from_directory, request
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

@app.route('/play', methods=['POST'])
def play():
    note = request.form.get('note')
    if note in ['G', 'D', 'A', 'E']:
        # Trigger the sound play for the note
        # Command to play the sound file using your existing script
        subprocess.run(['python', 'violin.py', note])
        return f"Playing {note}", 200
    return "Invalid note", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
