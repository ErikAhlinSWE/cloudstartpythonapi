from datetime import datetime, timezone
import random
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__= "Customer"
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), unique=False, nullable=False)
    City = db.Column(db.String(40), unique=False, nullable=False)
    TelephoneCountryCode = db.Column(db.Integer, unique=False, nullable=False)
    Telephone = db.Column(db.String(20), unique=False, nullable=False)
    
class Game(db.Model):
    __tablename__ = 'games'

    Id = db.Column(db.Integer, primary_key=True)
    CreatedAt = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    Winner = db.Column(db.String(50))
    YourSelection = db.Column(db.String(50))
    ComputerSelection = db.Column(db.String(50))
    
def seedData(db):
    cites = ["Stockholm","Västerås", "Södertälje"]
    countrycodes = [46,47,44]
    antal =  Customer.query.count()
    while antal < 100:
        customer = Customer()
        customer.Name = "Customer" + str(antal)
        customer.TelephoneCountryCode = random.choice(countrycodes)
        customer.Telephone = random.randint(10000000,999999999)
        customer.City = random.choice(cites)
        db.session.add(customer)
        db.session.commit()
        antal = antal + 1