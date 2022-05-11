from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from routes import EventsList, Event, UserList, User

app = Flask(__name__)
CORS(app)

api = Api(app)

BASE_URL = '/events/api'

api.add_resource(EventsList, f'{BASE_URL}/Events')
api.add_resource(Event, f'{BASE_URL}/Events/<event_id>')
api.add_resource(UserList, f'{BASE_URL}/Users')
api.add_resource(User, f'{BASE_URL}/Users/<event_id>')

if __name__ == '__main__':
    app.run(debug=True)