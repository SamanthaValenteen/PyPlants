from datetime import datetime, timedelta
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    plants = db.relationship('Plant', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(140))
    pot = db.Column(db.String(140))
    watering_frequency = db.Column(db.Integer) #in days
    last_watered = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    next_water_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def update_water_date(self): #separate function from water() for future scenarios, such as watering frequency being changed
        self.next_water_date = self.last_watered + timedelta(days=self.watering_frequency)

    def water(self):
        self.last_watered = datetime.utcnow()

    def __repr__(self):
        return '<Plant {}>'.format(self.type)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

