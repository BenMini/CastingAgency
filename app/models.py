from flask import json
from app import db


class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(db.Integer(), primary_key=True)
    title = Column(db.String(140))
    release_date = db.Column(db.DateTime, index=True)


class Actor(db.Model):
    __tablename__ = 'actors'
    id = Column(db.Integer(), primary_key=True)
    name = Column(db.String(140))
    age = Column(db.Integer(3))
    gender = Column(db.String(30))
