from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from routes import EventsList, Event, User
from psycopg2 import pool
import os

BASE_URL = os.environ.get("BASE_URL")
HOST = os.environ.get("HOST")
DATABASE = os.environ.get("DATABASE")
DB_PORT = os.environ.get("DB_PORT")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
MIN = os.environ.get("MIN")
MAX = os.environ.get('MAX')

app = Flask(__name__)
CORS(app)

app.config['pSQL_pool'] = pool.SimpleConnectionPool(MIN, MAX,
                                                    host=HOST,
                                                    database=DATABASE,
                                                    port=DB_PORT,
                                                    user=USER,
                                                    password=PASSWORD)


api = Api(app)


BASE_URL = os.environ.get("BASE_URL")

api.add_resource(EventsList, f'{BASE_URL}/events')
api.add_resource(Event, f'{BASE_URL}/events/<event_id>')
api.add_resource(User, f'{BASE_URL}/userInfo')


if __name__ == '__main__':
    app.run(debug=True)