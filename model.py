from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class userLogin(db.Model):
    __tablename__ = 'userLogin'  
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100))
    password=db.Column(db.String(100))
    email=db.Column(db.String(100))
    contact=db.Column(db.String(100))
    collegename=db.Column(db.String(1000))
    department=db.Column(db.String(100))

class events(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    eventname=db.Column(db.String(100))
    eventdate=db.Column(db.String(100))
    duration=db.Column(db.String(100))
    participants=db.Column(db.String(100))
    topics=db.Column(db.String(100))
    category=db.Column(db.String(100))

class registeredevents(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('userLogin.id'))  
    name=db.Column(db.String(100))
    dept=db.Column(db.String(100))
    interest=db.Column(db.String(100))
    selectedevent=db.Column(db.String(100))

class payment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    upi=db.Column(db.String(1000))
