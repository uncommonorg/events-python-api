from flask import Flask
from flask_restful import Api
from routes import ReviewList, Event, EventsList, Review

app = Flask(__name__)
api = Api(app)

BASE_URL = '/events/api'

api.add_resource(EventsList, f'{BASE_URL}/events')
api.add_resource(Event, f'{BASE_URL}/event/<event_id>')
api.add_resource(ReviewList, f'{BASE_URL}/reviews')
api.add_resource(Review, f'{BASE_URL}/review')

if __name__ == '__main__':
    app.run(debug=True)