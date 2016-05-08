from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    #User class that we just created contains several fields, defined as class variables. Fields are created as instances of the db.Column class, which takes the field type as an argument, plus other optional arguments that allow us, for example, to indicate which fields are unique and indexed.


    def __repr__(self):
        return '<User %r>' % (self.nickname)

    #__repr__ method tells Python how to print objects of this class. We will use this for debugging
