from flask import *
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
import os

from dotenv import load_dotenv
load_dotenv() # loads the environment variables

app = Flask(__name__)

# app.config['MONGODB_SETTINGS'] = {
#     'db': 'schedulify',
#     'host': 'localhost',
#     'port': 27017
# }
# db = PyMongo(app)

# class User(db.Document):
#     name = db.StringField()
#     email = db.StringField()
#     def to_json(self):
#         return {"name": self.name,
#                 "email": self.email}

app.secret_key = os.environ.get('SECRET_KEY')


app.config["MONGO_URI"] = f'mongodb://localhost:27017/schedulify'
mongo = PyMongo(app)

#User SignUp
def dbUserSignUp(name, email, password):
    result = mongo.db.users.insert_one({
            'name': name,
            'email': email,
            'password': password
    })
@app.route('/signup')
def signup():
   
    dbUserSignUp('Keval', 'keval@gmail.com', 'pass')

#User Login
def dbUserLogin(your_name, your_pass):
    result = mongo.db.users.insert_one({
            'your_name': your_name,
            'your_pass': your_pass,
            
    })

@app.route('/login')
def login():
   
    dbUserLogin('Keval', 'pass')
     

#Interviewer Login
def dbIntLogin(your_name, your_pass):
    result = mongo.db.users.insert_one({
            'your_name': your_name,
            'your_pass': your_pass,
            
    })

@app.route('/Intlogin')
def Intlogin():
   
    dbIntLogin('Keval', 'pass')
     

#Interviewer SignUp
def dbIntSignUp(your_name,email,organization,position, your_pass):
    result = mongo.db.users.insert_one({
            'your_name': your_name,
            'email':email,
            'organization':organization,
            'position':position,
            'password':your_pass
            
    })

@app.route('/IntSignUp')
def IntSignUp():
   
    dbIntSignUp('Keval', 'keval@gmail.com', 'Google', 'Software Engineer', 'pass')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/candidate-login')
def candidate_login():
    return render_template('candidate_login.html')

@app.route('/candidate-signup')
def candidate_signup():
    return render_template('candidate_signup.html')

@app.route('/recruiter-login')
def recruiter_login():
    return render_template('recruiter_login.html')

@app.route('/recruiter-signup')
def recruiter_signup():
    return render_template('recruiter_signup.html')

@app.route('/user_profile_form')
def user_profile_form():
    return render_template('user_profile_form.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)