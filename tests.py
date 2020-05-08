'''
Tests:
    - One test for success behavior of each endpoint
    - One test for error behavior of each endpoint
    - At least two test of RBAC for each role
'''
import os
import unittest
import json
from app import create_app, db
from app.models import Movie, Actor
from app.errors import handlers
from config import Config

executive_producer = os.environ['EXEC_PROD_JWT']
casting_director = os.environ['CAST_DIR_JWT']
casting_assistant = os.environ['CAST_ASSIST_JWT']


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


actor = {
    "name": "Brad Pitt",
    "age": 40,
    "gender": "male"
}

movie = {
    "title": "The Green Mile",
    "release_date": "1999-12-06"
}


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.actor = actor
        self.movie = movie

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

# -----------------------------------------------
# No Authentication Tests (GET '/actors' and '/movies')
# -----------------------------------------------
    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

# -----------------------------------------------
# Casting Assistant Tests
# -----------------------------------------------


if __name__ == '__main__':
    unittest.main(verbosity=2)
