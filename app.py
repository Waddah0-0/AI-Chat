from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

# Load API key from environment file
try:
    with open('API.env', 'r') as f:
        for line in f:
            if line.startswith('GEMINI_API_KEY='):
                API_KEY = line.split('=', 1)[1].strip()
                break
except FileNotFoundError:
    API_KEY = "AIzaSyATLRA10J6HAH0em0ShmAHWYsK7qC6SdJ0"  # fallback

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({'error': 'No message provided'}), 400
        
        chat = model.start_chat()
        response = chat.send_message(user_input)
        
        return jsonify({
            'response': response.text,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 