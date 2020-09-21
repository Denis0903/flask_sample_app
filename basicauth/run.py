from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask import render_template

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": "password",
    "guest": "password"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()

@auth.error_handler
def auth_error():
    return render_template('loginerror.html', title='Flask BasicAuth')

@app.route('/logout')
def logout():
    return render_template('logout.html'), 401

if __name__ == '__main__':
    app.run(debug=True, port=8888, threaded=True)
