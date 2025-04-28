from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    remarks = ''

    # Rules for a strong password
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.<br>"

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "Add at least one uppercase letter.<br>"

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "Add at least one lowercase letter.<br>"

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks += "Add at least one number.<br>"

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "Add at least one special character (!@#$ etc).<br>"

    # Final Evaluation
    if strength == 5:
        return "Very Strong Password!"
    elif strength >= 3:
        return "Moderate Password.<br>" + remarks
    else:
        return "Weak Password.<br>" + remarks

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form['password']
        result = check_password_strength(password)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
