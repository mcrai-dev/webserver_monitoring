from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer,  primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # controling_Log = db.relationship('Log', back_populates ='User')


# Log = db.Table('Log',
#                db.Column('Id', db.Integer, primary_key=True),
#                db.Column('Person', db.String(1000), db.ForeignKey('user.email')),
#                db.Column('Date_and_time', db.String(50)),
#                db.Column('Activity', db.String(1000))
#                )

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(50))
    name = db.Column(db.String(100) )
    activity = db.Column(db.String(1000))


class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rebour = db.Column(db.String(50))
    name_commander = db.Column(db.String(1000))
    def __repr__(self):
        return f'<Command: {self.name}>'

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    mac_address = db.Column(db.String(30) )
    def __repr__(self):
        return f'<Device: {self.name}>'