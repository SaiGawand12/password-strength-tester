from flask import Flask, request, jsonify, render_template
import re


app = Flask(__name__)

# Password strength functions (same as before)
def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

def check_lowercase(password):
    return bool(re.search(r'[a-z]', password))

def check_digit(password):
    return bool(re.search(r'\d', password))

def check_special_char(password):
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def check_common_patterns(password):
    common_patterns = ['password', '123456', 'qwerty', 'abc123', 'letmein']
    return not any(pattern in password.lower() for pattern in common_patterns)

def password_strength(password):
    strength = 0
    
    if check_length(password):
        strength += 1
    if check_uppercase(password):
        strength += 1
    if check_lowercase(password):
        strength += 1
    if check_digit(password):
        strength += 1
    if check_special_char(password):
        strength += 1
    if check_common_patterns(password):
        strength += 1
    
    if strength < 3:
        return "Weak"
    elif strength < 5:
        return "Moderate"
    else:
        return "Strong"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_password_strength', methods=['POST'])
def check_password():
    password = request.json.get('password', '')
    strength = password_strength(password)
    return jsonify({'strength': strength})

if __name__ == '__main__':
    app.run(debug=True)
