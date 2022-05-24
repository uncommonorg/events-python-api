from models import EventModel, ReviewModel
import psycopg2


event1 = EventModel("Tawanda","Africa day","Wednesday @12","fun","Dz",50, 1)
event2 = EventModel("David","Heros day","Thursday @1","fun","Dz",90, 1)

review1 = ReviewModel("reviewed by Tino","@1am", 1)
review2 = ReviewModel("reviewer by Tine","@", 2)
review3 = ReviewModel("reviewer by Tine", "@", 3)
review4 = ReviewModel("reviewer by Tine", "@", 4)

HOST = '127.0.0.1'
DATABASE = 'eventsapp'
DB_PORT = '5432'
USER = 'postgres'
PASSWORD = 'tawanda'

class Repository():
    
    def get_db(self):
        return psycopg2.connect(
                        host=HOST,
                        database=DATABASE,
                        port=DB_PORT,
                        user=USER,
                        password=PASSWORD)

    
    
    def events_get_all(self):
        try:
            conn = self.get_db()
            if (conn):
                 ps_cursor = conn.cursor()
                 ps_cursor.execute(" SELECT id, owner, title, event_time, description, location, likes, datetime_added order by datetime_added")
                 event_records = ps_cursor.fetchall()
                 event_list = []
                 for row in event_records:
                    event_list.append(EventModel(row[0], row[1], row[2],row[3]))
                 ps_cursor.close()
        
            return event_list
        except Exception as error:
                print(error)
        finally:
                if conn is not None:
                    conn.close()

    def book_get_by_id(self, data ):
        try:
            conn = self.get_db()
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute("INSERT INTO events(title,owner,description,location,event_time,likes,datetime_added) VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING eventId ",(data['title'], data['owner'], data['description'], data['location'], data['event_time'], data['likes'], data['datetime_added']))
                conn.commit()
                id = ps_cursor.fetchone()[0]
                ps_cursor.close() 
                event = EventModel(data['title'],id, data['owner'], data['description'], data['location'], data['event_time'], data['likes'], data['datetime_added'])
            return event
        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
  
                
    def event_add(self, data):
            conn = self.get_db()
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute("INSERT INTO events (owner, title, event_time, description, location) VALUES (%s, %s, %s) RETURNING eventId",(data['title'], data['owner'], data['description'], data['location'], data['event_time'], data['likes'], data['datetime_added']))       
                conn.commit()
                id = ps_cursor.fetchone()[0]
                ps_cursor.close()
                event = EventModel(data['title'],id, data['owner'], data['description'], data['location'], data['event_time'], data['likes'], data['datetime_added'])
            return event
                
        
    
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
    
    
        
        

            


    
        
    

    



  