from app import db

#creates a database model for the users
#based on 3 columns: id, nickname, email
#each column constructor takes different arguments regarding data
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)

    def _repr_(self):
        return '<User %r>' % (self.nickname)
