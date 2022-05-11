class EventModel():
    def __init__(self, title, content, created_at, id=-1):
        self.title = title
        self.content = content
        self.created_at = created_at
        self.eventId = id

class ReviewModel():
    def __init__(self, comment, created_at, eventId, id=-1):
        self.comment = comment
        self.created_at = created_at
        self.eventId = eventId
        self.id = id