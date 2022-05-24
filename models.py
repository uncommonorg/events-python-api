class EventModel():
    def __init__(self, title, description, location, likes, id=-1):
        self.title = title
        self.description = description
        self.likes = likes
        self.location = location
        self.id = id

class UserModel():
    def __init__(self, name, last_name, email, id=-1):
        self.name = name
        self.last_name  = last_name
        self.email = email
        self.id = id
        
   

