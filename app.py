from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from routes import EventsList, Event, ReviewList

app = Flask(__name__)
CORS(app)

api = Api(app)

BASE_URL = '/events/api'

api.add_resource(EventsList, f'{BASE_URL}/Events')
api.add_resource(Event, f'{BASE_URL}/Events/<event_id>')
api.add_resource(ReviewList, f'{BASE_URL}/reviews/<event_id>')

if __name__ == '__main__':
    app.run(debug=True)