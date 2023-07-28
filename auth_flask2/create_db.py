from __init__ import  db
from models import User, Log

marc = Log(name ='marc', email='marc@gmail.com')
db.session.add()
db.session.commit()
 