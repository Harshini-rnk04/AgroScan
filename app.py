from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'agroscan_secret_key'  # Needed for session

@app.route('/')
def index():
    return render_template('index.html')  # This is your homepage

@app.route('/set-role/<role>')
def set_role(role):
    session['role'] = role
    return redirect(url_for('select_role'))

@app.route('/select_role')
def select_role():
    role = session.get('role', 'user')
    return render_template('select_role.html', role=role)

@app.route('/login', methods=['GET', 'POST'])
def login():
    role = session.get('role', 'user')
    return render_template('login.html', role=role)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    role = session.get('role', 'user')
    return render_template('signup.html', role=role)

if __name__ == '__main__':
    app.run(debug=True)
