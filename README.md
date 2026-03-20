# Files: index.html, style.css, script.js, password_manager.py

# Description:
This project is a comprehensive security application designed to enforce strong password policies and provide instant feedback to users. It features a modern, responsive web interface that validates password complexity in real-time and a Python Flask backend that handles secure data processing and automated email notifications.

# Key Technical Features:
Real-Time Frontend Validation: Uses Regular Expressions (Regex) in JavaScript to instantly check password strength against specific criteria (length, uppercase, lowercase, numbers, and symbols) as the user types.

Secure Flask Backend: Implements a RESTful API endpoint (/create-password) using Flask and Flask-CORS to process user registrations securely.

Automated Email Integration: Features a built-in notification system using the SMTP library and SSL to send a confirmation email to the user once a strong password has been successfully registered.

Double-Layer Verification: For maximum security, password strength is validated both on the client-side (JS) and server-side (Python) to prevent unauthorized or weak entries.

Interactive UI/UX: Includes dynamic CSS styling to provide visual cues (green/red indicators) based on the validity of the user's input.

# Tech Stack:
Frontend: HTML5, CSS3, JavaScript (ES6).

Backend: Python, Flask.

Security & Utils: SMTP for email, Regex for pattern matching.
