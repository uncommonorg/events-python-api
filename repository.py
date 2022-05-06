from models import EventModel, ReviewModel
import psycopg2

event1 = EventModel("church service","Happening at goromonzi","@4pm", 1)
event2 = EventModel("party","happening in Harare","@2pm" ,2)

review1 = ReviewModel("reviewed by Tino","@1am", 1)
review2 = ReviewModel("reviewer by Tine","@", 2)
review3 = ReviewModel("reviewer by Tine", "@", 3)
review4 = ReviewModel("reviewer by Tine", "@", 4)

HOST = '127.0.0.1'
USER = 'postgres'
DB_PORT = 5432
DATABASE = 'bookreactions'
PASSWORD = 'precell'
class Repository():
    def get_db(self):
        return psycopg2.connect(
            host = HOST,
            database = DATABASE,
            user  = USER,
            password = PASSWORD,
            port = DB_PORT,
            
        )
        
    def events_get_all(self):
        conn = None
        try:
            conn = self.get_db()
            if(conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute(
                    "SELECT title, author, cover FROM book "
                )
                events_records = ps_cursor.fetchall()
                events_list = []
                for row in events_records:
                    events_list.append(EventModel(row[0], row[1], row[2]))  
                ps_cursor.close()
                return events_list
                 
        except Exception as error:
            print(error)
        finally:    
            if conn is not None:
                conn.close()
                
    def get_event_by_id(self, event_id):
        id = event_id
        conn = None
        try:
            conn = self.get_db()
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute(
                    f'SELECT title, author, cover FROM book WHERE bookId = {int(id)}'
                )
                event_record = ps_cursor.fetchone()
                ps_cursor.close()
                event = EventModel(event_record[0], event_record[1], event_record[2])
            return event
        except Exception as error:
            print(error)
        finally:      
            if conn is not None:
                conn.close()  
       
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


  