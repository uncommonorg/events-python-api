from flask_restful import Resource
from flask import request
from repository import Repository

repository = Repository()

class EventsList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self):
        return [event.__dict__ for event in self.repo.events_get_all()]
    
class Event(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def get(self, event_id):
        return self.repo.get_event_by_id(int(event_id)).__dict__
        
    def post(self):
        data = request.get_json()
        return self.repo.user_add(data).__dict__

class UserList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self):
        return [user.__dict__ for user in self.repo.users_get_all()]
    
class User(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def get(self, event_id):
        return self.repo.user_get_by_event_id(int(event_id)).__dict__

    def post(self):
       data = request.get_json()
       return self.repo.user_add(data).__dict__



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
