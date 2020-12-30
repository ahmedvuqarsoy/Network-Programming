from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)


# SESSION AUTHENTICATION
AUTHENTICATED = False


# HELPER FUNCTION



# MODELS for DB
class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    info = db.Column(db.String(100), nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    arrival = db.Column(db.DateTime, nullable=False, default=datetime.now)
    departure = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f"Flight(source = {self.source}, destination = {self.destination}, info = {self.info}, passengers = {self.passengers}, arrival = {self.arrival}, destination = {self.destination}"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


# REQUEST PARSING for POST request
flightArgs = reqparse.RequestParser()
flightArgs.add_argument('source', type=str, help="Source Point of the Flight")
flightArgs.add_argument('destination', type=str, help="Destination Point of the Flight")
flightArgs.add_argument('info', type=str, help="Destination Point of the Flight")
flightArgs.add_argument('passengers', type=int, help="Destination Point of the Flight")



# fields (to Change Object -> JSON (Serialazing))
flightDataFields = {
    'id': fields.Integer,
    'source': fields.String,
    'destination': fields.String,
    'info': fields.String,
    'passengers': fields.Integer,
    'arrival': fields.DateTime,
    'departure': fields.DateTime
}

# RESTful Resources
class FlightData(Resource):
    @marshal_with(flightDataFields)
    def get(self, source, destination):
        flightList = Flight.query.filter_by(source=source, destination=destination).all()
        print(flightList)
        return flightList



api.add_resource(FlightData,'/flights/<string:source>/<string:destination>')


# db.create_all()
# flight1 = Flight(source='Istanbul', destination='Baku', info='VIP Flight', passengers=300)
# db.session.add(flight1)
# db.session.commit()

# username = input("Please Write Your Username: ")
# password = input("Please Type Your Password: ")
# authenticate = User.query.filter_by(username=username, password=password).first()
# if authenticate:
#     AUTHENTICATED = True
#     print("Welcome to the Dashboard")
# else:
#     print("Incorrect credentials")


if __name__ == '__main__':
    app.run(debug=True)
