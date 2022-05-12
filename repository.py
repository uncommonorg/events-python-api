from models import EventModel, ReviewModel

event1 = EventModel("church service","Happening at goromonzi","@4pm", 1)
event2 = EventModel("party","happening in Harare","@2pm" ,2)

review1 = ReviewModel("reviewed by Tino","@1am", 1)
review2 = ReviewModel("reviewer by Tine","@", 2)
review3 = ReviewModel("reviewer by Tine", "@", 3)
review4 = ReviewModel("reviewer by Tine", "@", 4)

class Repository():
    def events_get_all
        conn = None
        try:
            conn = self.get_db()
            if(conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute(
                    "SELECT title, details, venue, likes, id FROM events order by id"
                )
                events_records = ps_cursor.fetchall()
                events_list = []
                for row in events_records:
                    events_list.append(EventModel(row[1], row[0], row[2], row[3], row[4]))  
                ps_cursor.close()
                events = [event3, event1, event2]
                return events_list
                 
        except Exception as error:
            print(error)
        finally:    
            if conn is not None:
                conn.close()
        
    users_table
    def users_get_all(self):
        conn = None
        try:
            conn = self.get_db()
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute(
                    'SELECT user_name, last_name, email, id from users'
                )
                users_records = ps_cursor.fetchall()
                users_list = []
                for row in users_records:
                    users_list.append(UserModel(row[0], row[1], row[2], row[3]))
                ps_cursor.close()
                users =  [user1, user2, user3, user4]
            return users_list      
        except Exception as error:
            print(error)
        finally:  
            if conn is not None:
                conn.close()     
        
        


  