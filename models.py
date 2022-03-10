from app import db
from flask_login import UserMixin
from  sqlalchemy.sql import func


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique=True)

class User_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email=db.Column(db.String(150),nullable=True)
    phone = db.Column(db.String(10),nullable=True)
    age = db.Column(db.String(2),nullable=True)
    address = db.Column(db.String(80),nullable=True)

    # appointment_date = db.Column(db.String(100))

    degree = db.Column(db.String(200),nullable=True)
    college = db.Column(db.String(100),nullable=True)
    clg_time = db.Column(db.String(15),nullable=True)
    cgpa = db.Column(db.String(3),nullable=True)
    cmpy_name = db.Column(db.String(100),nullable=True)
    cmpy_position = db.Column(db.String(100),nullable=True)
    cmpy_time = db.Column(db.String(100),nullable=True)
    cmpy_work = db.Column(db.String(100),nullable=True)
    skills_1 = db.Column(db.String(100),nullable=True)
    skills_2 = db.Column(db.String(100),nullable=True)
    skills_3 = db.Column(db.String(100),nullable=True)
    skills_4 = db.Column(db.String(100),nullable=True)
    skills_5 = db.Column(db.String(100),nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    appts = db.relationship('User_Info')
