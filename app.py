from flask import *
from flask_pymongo import PyMongo
# from flask_mongoengine import MongoEngine
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
    if result == None:
        return 0
    else:
        return 1

@app.route('/check-candidate-signup', methods=['POST'])
def check_candidate_signup():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        password = request.form['pass'].strip()
        res = dbUserSignUp(name, email, password)
        if res == 1:
            return redirect(url_for('main'))
        else:
            return 'Login Failed'

#User Login
def dbUserLogin(your_name, your_pass):
    result = mongo.db.users.find_one({
            'email': your_name,
            'password': your_pass,
    })
    if result is None:
        return 0
    else:
        return 1

@app.route('/check-candidate-login', methods=['POST'])
def check_candidate_login():
    if request.method == 'POST':
        email = request.form['your_name'].strip()
        password = request.form['your_pass'].strip()
        res = dbUserLogin(email, password)
        if res == 1:
            return redirect(url_for('main'))
        else:
            return 'Login Failed'
     

#Interviewer Login
def dbIntLogin(your_name, your_pass):
    result = mongo.db.recruiters.find_one({
            'email': your_name,
            'password': your_pass,
    })
    if result is None:
        return 0
    else:
        return 1

@app.route('/check-recruiter-login', methods=['POST'])
def check_recruiter_login():
   if request.method == 'POST':
        email = request.form['your_name'].strip()
        password = request.form['your_pass'].strip()
        res = dbIntLogin(email, password)
        if res == 1:
            return redirect(url_for('main'))
        else:
            return 'Login Failed'


#Interviewer SignUp
def dbIntSignUp(your_name,email,organization,position, your_pass):
    result = mongo.db.recruiters.insert_one({
            'your_name': your_name,
            'email':email,
            'organization':organization,
            'position':position,
            'password':your_pass
    })
    if result is None:
        return 0
    else:
        return 1

@app.route('/check-recruiter-signup', methods=['POST'])
def check_recruiter_signup():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        password = request.form['pass'].strip()
        org = request.form['org'].strip()
        pos = request.form['pos'].strip()
        res = dbIntSignUp(name, email, org, pos, password)
        if res == 1:
            return redirect(url_for('main'))
        else:
            return 'Registration Failed'

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

@app.route('/user-profile-form')
def user_profile_form():
    return render_template('user_profile_form.html')

@app.route('/main')
def main():
    return 'Main'

@app.route('/fetch-user-profile', methods=['POST'])
def fetch_user_profile():
    if request.method == 'POST':
        name = request.form['full_name'].strip()
        email=request.form['email'].strip()
        phone = request.form['phone'].strip()
        age = request.form['age'].strip()
        address = request.form['address'].strip()

        # appointment_date = db.Column(db.String(100))
        degree = request.form['qualification'].strip()
        college = request.form['college'].strip()
        clg_time = request.form['duration'].strip()
        cgpa = request.form['cgpa'].strip()
        cmpy_name = request.form['company_name'].strip()
        cmpy_position = request.form['position'].strip()
        cmpy_time = request.form['duration_exp'].strip()
        cmpy_work = request.form['work'].strip()
        skills_1 = request.form['skill1'].strip()
        skills_2 = request.form['skill2'].strip()
        skills_3 = request.form['skill3'].strip()
        skills_4 = request.form['skill4'].strip()
        skills_5 = request.form['skill5'].strip()

        #print(skills_1, skills_2, name, email)
        return '1'

@app.route('/user-display')
def user_display():
    return render_template('user_profile.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)