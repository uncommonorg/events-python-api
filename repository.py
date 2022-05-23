from models import EventModel, ReviewModel
from firebase_admin import auth
from flask import request
import json
import pyrebase

event1 = EventModel("church service","Happening at goromonzi","@4pm", 1)
event2 = EventModel("party","happening in Harare","@2pm" ,2)

review1 = ReviewModel("reviewed by Tino","@1am", 1)
review2 = ReviewModel("reviewer by Tine","@", 2)
review3 = ReviewModel("reviewer by Tine", "@", 3)
review4 = ReviewModel("reviewer by Tine", "@", 4)

users = [{'uid':1, 'name':'Tawanda Nhare'}]

class Repository():
    def events_get_all(self):
        return [event1, event2]

    def get_event_by_id(self, event_id):
        events = [event1, event2]
        return [x.__dict__ for x in events if x.eventId == event_id]
    
    def reviews_get_all(self):
        return [review1, review2]
        return next((x for x in events if x.eventId == event_id), None)

    def reviews_get_by_event_id(self, event_id):
        reviews = [review1,review2,review3,review4]
        return [x for x in reviews if x.eventId == event_id]

    def review_get_by_id(self, event_id):
        reviews = [review1, review2]
        return next((x for x in reviews if x.eventId == event_id), None)

    def review_add(self, data):
        return ReviewModel(data['content'], data['eventId'], 1)
    
    def userinfo():
        return {'data': users}, 200
    
    def signup():
        email = request.form.get('email')
        password = request.form.get('password')
        if email is None or password is None:
            return {'message': 'Error missing email or password'},400
        try:
            user = auth.create_user(
                email=email,
                password=password
            )
            return {'message': f'Successfully created user {user.uid}'},200
        except:
            return {'message': 'Error creating a user'},400
        
        
#  getting  a new token fro a valid user

    def token():
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = pb.auth().sign_in_with_email_and_password(email, password)
            jwt = user['idToken']
            return {'token': jwt}, 200
        except:
            return {'message': 'There was an error logging in'},400
            


    
        
    

    



  