# Schedulify
Interview scheduling is time-consuming and taxing. It requires a set of people or a trained person/secretary to do it, since multiple people such as interviewers/hiring managers, recruiters and candidates have to be taken into consideration.  
We built a progressive web application **Schedulify** that will help with scheduling interviews effortlessly faster, saving time.  
Made as a part of TSEC Hacks 2022 Hackathon.

**Tech Stack Used:** HTML5, CSS, JavaScript, Bootstrap 5, Flask  
**Database Used:** MongoDB, SQLAlchemy  
**Vector Illustrations:** Some vector illustrations used in this project are taken from [undraw.co](https://undraw.co/)  
**API Used:** Calendy used for Easy Scheduling

## Steps to run the app locally
* Install your desired version of [Python](https://www.python.org/downloads/) on your local system if not installed already.
* Install [PIP(Preferred Installer Program)](https://www.liquidweb.com/kb/install-pip-windows/). Though in newer versions, PIP is already installed.
* Install Python Virtual Environment by using the below command:
    > pip install virtualenv  
* Open command prompt (or terminal) and change the current working directory to location where you want to clone the repository.
* Then type: git clone [https://github.com/OptimalLearner/Schedulify.git](https://github.com/OptimalLearner/Schedulify.git)
* If the clone was successfully completed then a new sub directory may appear with the same name as the repository. Now change the current directory to the new sub directory.
* Create and activate a virtualenv by using the following commands:
    > virtualenv venv  
    > venv/Scripts/activate
* Install all the dependencies required to run the app:
    > $ pip install -r requirements.txt
* Create a `.env` file in the root directory and copy the contents of `.env.sample` file to the newly created .env file. Replace 'YOUR_SECRET_KEY' to your Secret Key.
* In case you set up MongoDB on your local system, change the MongoDB URI in the code with your MongoDB URI, and if you set up your database on MongoDB Atlas, change the environment variables in the .env file.
* Now run the app by using the below command:
    > python app.py
