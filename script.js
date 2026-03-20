document.addEventListener('DOMContentLoaded', function() {
  const loginForm = document.getElementById('loginForm');
  const passwordInput = document.getElementById('password');
  const passwordStrength = document.getElementById('passwordStrength');
  const messageDiv = document.getElementById('message');
  const emailInput = document.getElementById('email'); // <--- ADD THIS LINE

  function validatePassword(pass) {
    const strongRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return strongRegex.test(pass);
  }

  passwordInput.addEventListener('input', function() {
    const pass = this.value;
    if (validatePassword(pass)) {
      passwordStrength.textContent = 'Strong password!';
      passwordStrength.className = 'strength-text strength-strong';
    } else {
      passwordStrength.textContent = 'Password does not meet criteria.';
      passwordStrength.className = 'strength-text strength-weak';
    }
  });

  loginForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value.trim();
    const password = passwordInput.value;
    const email = emailInput.value.trim(); // <--- ADD/MODIFY THIS LINE TO GET EMAIL VALUE

    // <--- MODIFY THIS LINE TO INCLUDE EMAIL CHECK
    if (validatePassword(password) && username !== '' && email !== '') {
      // Send data to backend
      fetch('http://127.0.0.1:5000/create-password', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: username,
          password: password,
          email: email // <--- ADD THIS LINE TO SEND EMAIL TO BACKEND
        })
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          messageDiv.textContent = data.message;
          messageDiv.className = 'message message-success';
        } else {
          messageDiv.textContent = data.message + (data.missing ? ' Missing: ' + data.missing.join(', ') : '');
          messageDiv.className = 'message message-error';
        }
      })
      .catch(error => {
        messageDiv.textContent = 'Error communicating with server.';
        messageDiv.className = 'message message-error';
      });
    } else {
      messageDiv.textContent = 'Please fill in all fields and create a strong password.';
      messageDiv.className = 'message message-error';
    }
  });
});