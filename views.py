from flask import Blueprint, Flask, render_template ,request,flash,jsonify,redirect,url_for
from flask_login import login_user, login_required , current_user
from .models import *
from . import db
import  json

#from . import  mail ,Message



views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/login_home', methods=['GET','POST'])
@login_required
def login_home():
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


        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Email are not same. ', category='error')

        elif len(email) < 4:
            flash('Email must be greater than 3 character.', category='error')

        elif len(name) < 2:
            flash('First name must be greater than 1  character.', category='error')



        elif len(phone) < 7:
            flash('Phone number must be more than that it should be up to 10', category='error')

        else:
            new_appoint = User_Info(name=name, email=email, phone=phone, age=age,address=address,degree=degree, college=college, clg_time=clg_time,  cgpa=cgpa, cmpy_name=cmpy_name, cmpy_position=cmpy_position,  cmpy_time=cmpy_time,  cmpy_work=cmpy_work, skills_1 =skills_1,skills_2 =skills_2 ,skills_3 =skills_3,skills_4 =skills_4,skills_5 =skills_5,user_id=current_user.id)
            db.session.add(new_appoint)
            db.session.commit()
            pass

            flash('Appointment made you will hear from us shortly!!', category='success')
            print("yes its working")
            return redirect(url_for('views.login_home'))

    return render_template("user_profile_details.html")


@views.route('/information_insertion', methods=['GET','POST'])
def information_insertion():
    if request.method == "POST":
        note = request.form.get('note')

        if  len(note) < 1:
            flash('information description is short !!!', category='error')

        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()

            flash('Information Added!!', category='success')
    return render_template('info.html', user=current_user)


@views.route('/Doctor_page')
def Doc_pg():
   # appointment = request.data('appointment')
    temp = User_Info.query.all()
    print(temp)
    temp2 = Note.query.all()
    return render_template('Docmain.html', appoint=temp, info = temp2 )


@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)

    noteId= note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
