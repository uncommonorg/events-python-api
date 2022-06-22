from flask import request
from routes import Event, EventsList, Review
from repository import Repository
from unittest.mock import MagicMock
from models import EventModel, ReviewModel

event1 = EventModel("church service","Happening at goromonzi","@4pm", 1)
event2 = EventModel("party","happening in Harare","@2pm" ,2)

review1 = ReviewModel("reviewed by Tino","09-03-2022", 1)
review2 = ReviewModel("reviewer by Tine","02-03-2022", 2)



def test_event_get():
    repo = MagicMock(spec=Repository)
    repo.get_event_by_id.return_value = event2
    event = Event(repo).get(1)
    assert int(event['eventId']) == 2
    assert event['title'] == 'party'
    
def test_review_get():
    repo = MagicMock(spec=Repository)
    repo.get_review_by_id.return_value = review1
    review = Review(repo).get(1)
    assert int(review['eventId']) == 2
    assert review['comment'] == 'reviewer by Tine'
    
def test_EventsList_get():
    repo = MagicMock(spec=Repository)
    repo.events_get_all.return_value = [event1, event2]
    events = EventsList(repo).get()
    assert events[0]['id'] == 1
    assert events[1]['title'] == 'Test church service'
