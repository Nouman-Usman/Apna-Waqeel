import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key')

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'True') == 'True'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'noumanmughal0123@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'jpvp jnni dljo mjjf')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'noumanmughal0123@gmail.com')

mail = Mail(app)

@app.route('/')
def index():
    return render_template('try.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['subscribe-form-email']
    msg = Message('New Subscription', recipients=['noumanusman.uet@gmail.com'])
    msg.body = f'New subscription from: {email}'
    mail.send(msg)
    return jsonify({'message': 'Subscription successful!'}), 200

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['form-message']
    msg = Message('New Query', recipients=['noumanusman.uet@gmail.com'])
    msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    mail.send(msg)
    return jsonify({'message': 'Message sent successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)