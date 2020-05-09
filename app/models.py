from flask import json
from app import db


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(140))
    release_date = db.Column(db.Date, index=True)

    def __repr__(self):
        return f'<Movie {self.id} {self.title} {self.release_date}>'

    def short(self):
        return {
            'id': self.id,
            'title': self.title,
        }

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(140))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(30))

    def __repr__(self):
        return f'<Actor {self.id} {self.name} {self.gender}>'

    def short(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
