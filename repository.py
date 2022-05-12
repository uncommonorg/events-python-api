from models import EventModel, UserModel
import psycopg2

event1 = EventModel("church service","Child dedication","24/08/22", "Sunshine Gardens", 1)
event2 = EventModel("Birthday","Celebrating John Doe 25th birthday","29/08/22", "EastGate Harare", 1)
event3 = EventModel("Managers workshop","Discuss the goals for the year","01/09/22", "Mfakose Hub", 1)

user1 = UserModel("John", "Doe", "jdoe@gmail.com", 1)
user2 = UserModel("Jane", "Doe", "jaydoe@gmail.com", 1)
user3 = UserModel("Katt", "Williams", "kattwill@gmail.com", 1)
user4 = UserModel("Abraham", "Lincoln", "ablinc@gmail.com", 2)



HOST = '127.0.0.1'
USER = 'postgres'
DB_PORT = 5432
DATABASE = 'eventsdb'
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
                    "SELECT title, details, id, venue, likes, created_at FROM events order by id"
                )
                events_records = ps_cursor.fetchall()
                events_list = []
                for row in events_records:
                    events_list.append(EventModel(row[0], row[1], row[3], row[3 ], row[2]))  
                ps_cursor.close()
                events = [event3, event1, event2]
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
                    f'SELECT title, details, venue, likes, id FROM events WHERE id = {int(id)}'
                )
                event_record = ps_cursor.fetchone()
                ps_cursor.close()
                event = EventModel(event_record[0], event_record[1], event_record[3], event_record[2], event_record[2])
            return event
        except Exception as error:
            print(error)
        finally:      
            if conn is not None:
                conn.close()  
       
    def event_add(self, data):
        return EventModel(data['title'], data['description'], data['date'], data['venue'], 2)
       
    
    def users_get_all(self):
        users =  [user1, user2, user3, user4]
        return users

    def user_get_by_event_id(self, event_id):
        users =  [user1, user2, user3, user4]
        return [x.__dict__ for x in users if x.id == event_id]

    def user_add(self, data):
        return UserModel(data['name'], data['last_name'], data['email'], 1)

    # def review_get_by_id(self, event_id):
    #     users =  [user1, user2, user3, user4]
    #     return next((x for x in users if x.eventId == event_id), None)

    

  