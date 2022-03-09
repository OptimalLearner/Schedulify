from flask import *
from flask_pymongo import PyMongo

import os

from dotenv import load_dotenv
load_dotenv() # loads the environment variables

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

app.config["MONGO_URI"] = f'mongodb://{os.environ.get("MONGO_USER")}:{os.environ.get("MONGO_PASSWORD")}@cluster0-shard-00-00.pcszv.mongodb.net:27017,cluster0-shard-00-01.pcszv.mongodb.net:27017,cluster0-shard-00-02.pcszv.mongodb.net:27017/{os.environ.get("MONGO_DB")}?ssl=true&replicaSet=atlas-duk28h-shard-0&authSource=admin&retryWrites=true&w=majority'
mongo = PyMongo(app)

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)