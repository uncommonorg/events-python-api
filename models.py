class EventModel():
    def __init__(self,  owner,title,  event_time,description ,location, likes,datetime_added, id=-1):
        self.owner = owner
        self.title = title
        self. event_time=  event_time
        self.description = description 
        self.location = location
        self.likes = likes
        self.datetime_added = datetime_added
        self.eventId = id

class ReviewModel():
    def __init__(self, comment, created_at, eventId, id=-1):
        self.comment = comment
        self.created_at = created_at
        self.eventId = eventId
        self.id = id
        

class UserModel():
    def _init_(self, name, last_name, email, id=-1):
        self.name = name
        self.last_name  = last_name
        self.email = email
        self.id = id    
        
    