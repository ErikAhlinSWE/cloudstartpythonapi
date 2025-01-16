# hej
from flask import Flask, render_template, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
from random import randint
from appconfig.config import DevelopmentConfig, ProductionConfig
from model import db, seedData, Customer
import os
    # - docker build -t git.systementor.se/yacloud/yagolangapi .
    #   - docker login -u yacloud -p yacloud1 https://git.systementor.se
    #   - docker push git.systementor.se/yacloud/yagolangapi 
# köra den i vårt linoide kluster
# bygga docker image -> git.systementor.se
# skapa en databas
# sätta upp subdomain
# mappa -> ingress -> service -> deployments

app = Flask(__name__)

if os.getenv('RUNENVIRONMENT') == "Production":
    app.config.from_object(ProductionConfig())
else:
    app.config.from_object(DevelopmentConfig())


# Go -> ORM -> GORM 
# Python Flask, flask_sqlalchemy -> Sqlalchemy 
# mysql / sqlite

db.app = app 
db.init_app(app)
migrate = Migrate(app,db)

@app.route("/api/customer/<id>")
def apiCustomer(id):
    c = Customer.query.filter_by(Id=id).first_or_404()
    # select * from customer where id=@id
    return jsonify({ "Id": c.Id, 
                 "Name":c.Name, 
                 "City":c.City,
                  "TelephoneCountryCode":c.TelephoneCountryCode,
                   "Telephone":c.Telephone })


@app.route("/api/customer/<id>", methods=["PUT"])
def apiCustomerUpdate(id):
    data = request.get_json()
    c = Customer.query.filter_by(Id=id).first_or_404()
    c.City = data["City"]
    c.Name = data["Name"]
    c.Telephone = data["Telephone"]
    c.TelephoneCountryCode = data["TelephoneCountryCode"]
    db.session.commit()
    return jsonify({ "Id": c.Id, 
                 "Name":c.Name, 
                 "City":c.City,
                  "TelephoneCountryCode":c.TelephoneCountryCode,
                   "Telephone":c.Telephone }), 200

@app.route("/api/customer", methods=["POST"])
def apiCustomerCreate():
    data = request.get_json()
    c = Customer()
    c.City = data["City"]
    c.Name = data["Name"]
    c.Telephone = data["Telephone"]
    c.TelephoneCountryCode = data["TelephoneCountryCode"]
    db.session.add(c)
    db.session.commit()
    return jsonify({ "Id": c.Id, 
                 "Name":c.Name, 
                 "City":c.City,
                  "TelephoneCountryCode":c.TelephoneCountryCode,
                   "Telephone":c.Telephone }), 201


@app.route("/api/customer")
def apiCustomers():
    lista = []
    for c in Customer.query.all():
        cdict = { "Id": c.Id, 
                 "Name":c.Name, 
                 "City":c.City }
        lista.append(cdict)
 
    return jsonify(lista)

@app.route("/customers")
def contactpage():
    s = "<html><head><title>Get lost</title></head><body>"
    for c in Customer.query.all():
        s = s + c.Name + "<br />"
    s = s + "</body></html>"
    return s

#if __name__  == "__main__":
with app.app_context():
#    db.create_all()
#    upgrade()

#    seedData(db)
    app.run()