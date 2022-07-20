from flask import Flask, g
from flask_restful import Api
from flask_cors import CORS
import psycopg2
from routes import EventsList, Event, UserList, User
import os
from psycopg2 import pool

app = Flask(__name__)
CORS(app)

api = Api(app)

BASE_URL = os.environ.get("BASE_URL")
# BASE_URL = os.environ.get("BASE_URL")
MIN = os.environ.get("MIN")
MAX = os.environ.get("MAX")
USER = os.environ.get("USER")
HOST = os.environ.get("HOST")
PASSWORD = os.environ.get("PASSWORD")
DB_PORT = os.environ.get("DB_PORT")
DATABASE = os.environ.get("DATABASE")
DEBUG = os.environ.get("DEBUG")

app.config['pSQL_pool'] = pool.SimpleConnectionPool(MIN,
                                            MAX,
                                            user = USER,
                                            host = HOST,
                                            database = DATABASE,
                                            password = PASSWORD,
                                            port = DB_PORT)

api.add_resource(EventsList, f'{BASE_URL}/Events')
api.add_resource(Event, f'{BASE_URL}/Events/<event_id>')
api.add_resource(UserList, f'{BASE_URL}/Users')
api.add_resource(User, f'{BASE_URL}/Users/<event_id>')
# print(app.config['pSQL_pool'])

@app.teardown_appcontext
def close_conn(e):
    db = g.pop('db', None)
    if db is not None:
        app.config['pSQL_pool'].putconn(db)
        print('The connection was released to the pool')
if __name__ == '__main__':
    app.run(debug=DEBUG)