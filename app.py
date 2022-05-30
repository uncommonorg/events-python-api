from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from routes import EventsList, Event, User

app = Flask(__name__)
CORS(app)

api = Api(app)


BASE_URL = '/events/api'

api.add_resource(EventsList, f'{BASE_URL}/events')
api.add_resource(Event, f'{BASE_URL}/events/<event_id>')
api.add_resource(User, f'{BASE_URL}/userInfo')


if __name__ == '__main__':
    app.run(debug=True)