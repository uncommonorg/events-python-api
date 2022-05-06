class EventModel():
    def __init__(self, title, description, date, venue, created_at, id=-1):
        self.title = title
        self.description = description
        self.created_at = created_at
        self.date = date
        self.venue = venue
        self.eventId = id

class UserModel():
    def __inti__(self, name, last_name, email, id):
        self.name = name
        self.last_name  = last_name
        self.email = email
        self.id = id

