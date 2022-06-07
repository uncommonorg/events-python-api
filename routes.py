from flask_restful import Resource
from flask import request, abort
from repository import Repository

import auth



repository = Repository()

class EventsList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self):
        # need authentication here
        try:
            print('checking user has logged in')
            user_email = auth.authorize(request)
            print("The user email was verified as %s".format(user_email))
        except Exception: 
            # If we get here, then authentication failed, abort the operation
            abort(403)
        return [event.__dict__ for event in self.repo.events_get_all()]
    
class Event(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def get(self, event_id):
        return self.repo.get_event_by_id(int(event_id))
        
    def post(self):
        data = request.get_json()
        return self.repo.event_add(data).__dict__


class User(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def post(self, data):
        data = request.get_json()
        return self.repo.user_add(data).__dict__
    
# class ReviewList(Resource):
#     def __init__(self, repo=repository):
#         self.repo = repo
        
#     def get(self):
#         return [review.__dict__ for review in self.repo.reviews_get_all()]
    
# class Review(Resource):
#     def __init__(self, repo=repository):
#         self.repo = repo

#     def get(self):
#         return [review.__dict__ for review in self.repo.reviews_get_all()]

#     def post(self):
#        data = request.get_json()
#        return self.repo.review_add(data).__dict__
   

    



# from flask_restful import resource  
# from flask import request
# from repository import Repository
# from models import EventModel, ReviewModel

# repo = Repository()

# class EventsList(resource):
#     def get(self):
#         return {'hello': 'from EventsList'}

# class Event(resource):
#     def get(self, event_id):):
#         return {'hello': f'from Event {event_id}'}

# class ReviewList(resource):
#     def get(self, event_id):
#         return {'hello': f' from reviews for event {event_id}'}

# class Review(resource):
#     def __init__(self, repo=Repository):
#         self.repo = repo

#     def get(self, review_id)):
#         return {'hello': f'from review {review_id}'}
    
#     def post(self):
#        data = request.get_json()
#        return self.repo.review_add(data).__dict__
