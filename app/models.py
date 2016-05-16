from app import db
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)
"""



class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)


# We have added the Post class, which will represent blog posts written by users. The user_id field in the Post class was initialized as a foreign key, so that Flask-SQLAlchemy knows that this field will link to a user.

#Note that we have also added a new field to the User class called posts, that is constructed as a db.relationship field. This is not an actual database field, so it isn't in our database diagram. For a one-to-many relationship a db.relationship field is normally defined on the "one" side. With this relationship we get a user.posts member that gets us the list of posts from the user. The first argument to db.relationship indicates the "many" class of this relationship. The backref argument defines a field that will be added to the objects of the "many" class that points back at the "one" object. In our case this means that we can use post.author to get the User instance that created a post.

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)
