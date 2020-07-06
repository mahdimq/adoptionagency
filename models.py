from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Model schema to show pets for adoption"""
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default="https://tinyurl.com/y7wjf6tk")
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    is_available = db.Column(db.Boolean, nullable=False, default=True)
