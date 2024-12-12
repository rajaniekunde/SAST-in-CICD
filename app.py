# app.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to SAST Demo!"

@app.route('/greet', methods=['GET'])
def greet():
    user_input = request.args.get('name')
    # Vulnerable to XSS if user input is not sanitized
    return f"Hello, {user_input}!"

if __name__ == '__main__':
    app.run(debug=True)
