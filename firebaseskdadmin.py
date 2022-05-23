
from email.policy import default
from weakref import ref
import firebase_admin
from firebase_admin import credentials
# from firebase_admin import db
from firebase_admin import auth

cred = credentials.Certificate("./dz-events-app-firebase-adminsdk-srrcz-f96fbe630a.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseUR':'https://dz-events-app-default-rtdb.firebaseio.com/'
})

uid = "some uid"


ref = db.reference("/")
ref.set({
    'Employee':{
        'emp1':{
            'name':'Tawanda',
            'lname':'Nhrae',
            'age':'29'
        },
          'emp2':{
            'name':'David',
            'lname':'Nhrae',
            'age':'29'
        },
    }
})



# ref = db.reference("/Employee")
emp_ref = ref.child("emp1")

emp_ref.update({
    
})
