from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION-MANAGER-ADMIN'] = False
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
    arrival = db.Column(db.String(100), nullable=False, default=datetime.now)
    departure = db.Column(db.String(100), nullable=False, default=datetime.now)

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


# ---------- LOGIN ----------#
authArgs = reqparse.RequestParser()
authArgs.add_argument('username', type=str, help="Username of the authenticated user.", required=True)
authArgs.add_argument('password', type=str, help="Password of the authenticated user.", required=True)

class Login(Resource):
    def get(self):
        print(app.config['SESSION-MANAGER-ADMIN'])
        return {'authenticated': app.config['SESSION-MANAGER-ADMIN']}

    def post(self):
        args = authArgs.parse_args()
        user = User.query.filter_by(username=args['username'], password=args['password']).first()
        if(user):
            app.config['SESSION-MANAGER-ADMIN'] = True
            return {'authenticated': app.config['SESSION-MANAGER-ADMIN']}
        else:
            return {'authenticated': app.config['SESSION-MANAGER-ADMIN']}

api.add_resource(Login, '/authentication_authorization')
# ---------- ----- ----------#


# ---------- LOGOUT ----------#
class Logout(Resource):
    def get(self):
        app.config['SESSION-MANAGER-ADMIN'] = False
        return {'authenticated': app.config['SESSION-MANAGER-ADMIN']}

api.add_resource(Logout, '/end_session')
# ---------- ------ ----------#



# ---------- ADD/DELETE/UPDATE ----------#
addFlightFields = {
    'source': fields.String,
    'destination': fields.String,
    'info': fields.String,
    'passengers': fields.Integer,
    'arrival': fields.DateTime,
    'departure': fields.DateTime
}

postArgs = reqparse.RequestParser()
postArgs.add_argument('source', type=str, help="Source City (like: Baku)", required=True)
postArgs.add_argument('destination', type=str, help="Destination City (like: Baku)", required=True)
postArgs.add_argument('info', type=str, help="Information about Flight (like: Business)", required=True)
postArgs.add_argument('passengers', type=int, help="The Number of Passengers", required=True)
postArgs.add_argument('arrival', type=str, help="Arrivval Time and Date (2020-12-31 23:00:00)", required=True)
postArgs.add_argument('departure', type=str, help="Departure Time and Date (2020-12-31 23:00:00)", required=True)


putArgs = reqparse.RequestParser()
putArgs.add_argument('id', type=int, help="The Number of Passengers")
putArgs.add_argument('source', type=str, help="Source City (like: Baku)")
putArgs.add_argument('destination', type=str, help="Destination City (like: Baku)")
putArgs.add_argument('info', type=str, help="Information about Flight (like: Business)")
putArgs.add_argument('passengers', type=int, help="The Number of Passengers")
putArgs.add_argument('arrival', type=str, help="Arrivval Time and Date (2020-12-31 23:00:00)")
putArgs.add_argument('departure', type=str, help="Departure Time and Date (2020-12-31 23:00:00)")

class ManipulateFlight(Resource):

    def post(self):
        args = postArgs.parse_args()
        flight = Flight(source=args['source'], destination=args['destination'], info=args['info'], passengers=args['passengers'], arrival=args['arrival'], departure=args['departure'])
        db.session.add(flight)
        db.session.commit()
        return {'request': 'POST request is successful.'}, 201

    def put(self):
        args = putArgs.parse_args()
        id = args['id']
        flight = Flight.query.filter_by(id=id).first()
        if(flight):
            if args['source']:
                flight.source = args['source']
            if args['destination']:
                flight.destination = args['destination']
            if args['info']:
                flight.info = args['info']
            if args['passengers']:
                flight.passengers = args['passengers']
            if args['arrival']:
                flight.arrival = args['arrival']
            if args['departure']:
                flight.departure = args['departure']

            
            db.session.commit()

            return {'200': 'The file is updated.'}
        
        else:
            abort(404, f"The flight with ID Number {id} cannot found.")


    def delete(self):
        pass


api.add_resource(ManipulateFlight, '/flights')



# ---------- ----------------- ----------#


if __name__ == '__main__':
    app.run(debug=True)
