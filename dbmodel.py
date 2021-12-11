from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean)

    def __repr__(self):
        return f"User('{self.email}'"

    class Note(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        note = db.Column(db.String(200))
        categories db.Column(db.String(200))
        user_id = db.Column(db.String(50))
