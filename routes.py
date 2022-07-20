from flask_restful import Resource
from flask import request
from repository import Repository

repository = Repository()

class EventsList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self):
        # return 'precell'
        return [event.__dict__ for event in self.repo.events_get_all()]
    
class Event(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def get(self, event_id):
        return self.repo.get_event_by_id(int(event_id)).__dict__
        
    def post(self):
        data = request.get_json()
        return self.repo.event_add(data).__dict__

class UserList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self):
        return [user.__dict__ for user in self.repo.users_get_all()]
    
    def post(self, req=request):
       data = req.get_json()
       return self.repo.user_add(data).__dict__

class User(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def get(self, event_id):
        return self.repo.user_get_by_event_id(int(event_id))


