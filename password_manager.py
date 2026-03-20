# password_manager.py
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Email configuration (replace with your details)
sender_email = "ap.anamika005@gmail.com"  # Your Gmail
sender_password = "ronwamyrvguqmhhf"      # Your App Password
# REMOVE OR COMMENT OUT THIS LINE: recipient_email = "rajnishkumar6054@gmail.com"

def is_strong_password(password):
    criteria = {
        "length >= 8": len(password) >= 8,
        "uppercase letter": re.search(r'[A-Z]', password) is not None,
        "lowercase letter": re.search(r'[a-z]', password) is not None,
        "digit": re.search(r'\d', password) is not None,
        "special character": re.search(r'[!@#$%^&*]', password) is not None
    }
    return all(criteria.values()), criteria

def send_email(to_email, password_created):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = "Password Creation Successful"
    body = f"Hello,\n\nYou have successfully created a strong password!\n\nYour password was: {password_created}\n\nNote: For security, never share your password."
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

@app.route('/create-password', methods=['POST'])
def create_password():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')  # <--- MODIFY THIS LINE TO GET EMAIL FROM THE FRONTEND REQUEST

    if not email: # <--- ADD THIS BASIC VALIDATION FOR EMAIL PRESENCE
        return jsonify({"success": False, "message": "Email is required."}), 400

    is_strong, criteria = is_strong_password(password)
    if not is_strong:
        missing = [k for k, v in criteria.items() if not v]
        return jsonify({"success": False, "message": "Password does not meet all criteria.", "missing": missing}), 400

    # Send email to the provided email address
    if send_email(email, password): # <--- THIS LINE WILL NOW USE THE 'email' VARIABLE
        return jsonify({"success": True, "message": "Password created and email sent!"})
    else:
        return jsonify({"success": False, "message": "Password created, but failed to send email."}), 500

if __name__ == "__main__":
    app.run(debug=True)