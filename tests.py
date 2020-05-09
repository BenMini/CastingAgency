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
from flask_sqlalchemy import SQLAlchemy
from app.models import Movie, Actor
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client

        self.app_context = self.app.app_context()
        self.app_context.push()

        self.CASTING_ASSISTANT_HEADER = {
            'Authorization': 'bearer ' + os.environ['CAST_ASSIST_JWT']
        }
        self.CASTING_DIRECTOR_HEADER = {
            'Authorization': 'bearer ' + os.environ['CAST_DIR_JWT']
        }
        self.EXEC_PRODUCER_HEADER = {
            'Authorization': 'bearer ' + os.environ['EXEC_PROD_JWT']
        }
        self.actor = {
            "name": "Tom Cruise",
            "age": 40,
            "gender": "male"
        }
        self.movie = {
            "title": "The Green Mile",
            "release_date": "1999-12-06"
        }

        db.create_all()

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
# Executive Producer Tests
# -----------------------------------------------
    def test_ep_post_movie(self):
        res = self.client().post(
            '/actors', headers=self.EXEC_PRODUCER_HEADER,
            json=self.movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
# -----------------------------------------------
# Casting Assistant Tests
# -----------------------------------------------

    def test_ca_get_actor_info(self):
        res = self.client().get(
            '/actors/1', headers=self.CASTING_ASSISTANT_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('actors' in data)

    def test_ca_get_movie_info(self):
        res = self.client().get(
            '/movies/1', headers=self.CASTING_ASSISTANT_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('movies' in data)

    def test_ca_post_actor_error(self):
        res = self.client().post(
            '/actors', headers=self.CASTING_ASSISTANT_HEADER)
        data = json.loads(res.data)
        self.assertNotEqual(res.status_code, 200)
        self.assertFalse('actors' in data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
