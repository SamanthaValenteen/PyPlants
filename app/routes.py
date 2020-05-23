from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, PlantForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Plant
from werkzeug.urls import url_parse
from datetime import timedelta, datetime


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PlantForm()
    if form.validate_on_submit():
        new_plant = Plant(type=form.type.data, pot=form.pot.data, watering_frequency=form.watering_frequency.data, user_id=current_user.id, next_water_date=datetime.utcnow() + timedelta(days=form.watering_frequency.data))
        db.session.add(new_plant)
        db.session.commit()
        flash('New plant added!')
        return redirect(url_for('index'))

    plants = Plant.query.filter_by(user_id=current_user.id)
    plant_list = []
    # This loop to update my existing table that didn't have water date populated.
    for plant in plants:
        plant.update_water_date()
        plant_list.append(plant.type)
    print(plant_list)
    plant_count = Plant.query.filter_by(user_id=current_user.id).count()

    #TODO add form to update watering date or other properties.
    #update_form = UpdatePlantForm()

    return render_template('index.html', title='Home', plants=plants, form=form, plant_count=plant_count)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title="sign In", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)