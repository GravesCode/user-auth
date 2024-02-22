from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Hash authentication performed using SCRYPT - modern hashing algorithm
# Details here: https://werkzeug.palletsprojects.com/en/2.3.x/utils/#module-werkzeug.security
# stores result to be compared against check_password_hash
user_db = {
    "user1": generate_password_hash("abc123"),
}

#check_password_hash compares provided password with generated password hash
@auth.verify_password
def verify_password(username, password):
    if username in user_db and \
            check_password_hash(user_db.get(username), password):
        return username
    return None

@app.route('/login')
@auth.login_required
def index():
    return jsonify({"message": "Authentication successful!"})

#TODO: Figure out why this doesn't work
#@auth.error_handler(401)
#def custom_401():
#    response = jsonify({username:password})
#    return response, 401

if __name__ == '__main__':
    app.run()
