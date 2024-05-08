
from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Database (in-memory)
users = []

# Function to generate a random OTP
def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

# Home page - User Registration form
@app.route('/')
def home():
    return render_template('Web appl.html')

# User Registration endpoint
@app.route('/register', methods=['POST'])
def register():
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    username = request.form.get('username')
    email = request.form.get('email')

    # Generate OTP
    otp = generate_otp()

    # Save user details in the database
    user = {
        'firstName': firstName,
        'lastName': lastName,
        'username': username,
        'email': email,
        'otp': otp
    }
    users.append(user)

    # Send verification email to the user (you need to implement the email sending functionality)

    return jsonify({'status': 'success', 'email': email})

# OTP Verification page
@app.route('/verify/<email>')
def verify(email):
    return render_template('verify.html', email=email)

# OTP Verification endpoint
@app.route('/verify', methods=['POST'])
def verify_otp():
    email = request.form.get('email')
    otp = request.form.get('otp')

    # Find the user in the database
    user = next((user for user in users if user['email'] == email), None)

    if user and user['otp'] == otp:
        return 'Hello, {}!'.format(user['username'])
    else:
        return 'OTP verification failed.'

if __name__ == '__main__':
    app.run(debug=True)
