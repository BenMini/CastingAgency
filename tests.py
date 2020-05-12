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
    SQLALCHEMY_DATABASE_URI = "postgres://{}/{}".format(
        'localhost:5432', "test_capstone")


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

        db.create_all()
        a = Actor(name='Tom Cruise', age=40, gender='male')
        db.session.add(a)
        db.session.commit()
        m = Movie(title='The Green Mile', release_date='2019-01-01')
        db.session.add(m)
        db.session.commit()

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
    def test_a_ep_post_movie(self):
        res = self.client().post(
            '/movies', headers=self.EXEC_PRODUCER_HEADER,
            json={
                "title": "Shawshank Redemption",
                "release_date": "1994-09-22"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_b_ep_post_actors(self):
        res = self.client().post(
            '/actors', headers=self.EXEC_PRODUCER_HEADER,
            json={
                "name": "Natalie Portman",
                "age": 38,
                "gender": "female"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_c_ep_get_actor_info(self):
        res = self.client().get(
            '/actors/1', headers=self.EXEC_PRODUCER_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('actors' in data)

    def test_d_ep_get_movie_info(self):
        res = self.client().get(
            '/movies/1', headers=self.EXEC_PRODUCER_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('movies' in data)

    def test_e_ep_patch_movie(self):
        res = self.client().patch(
            '/movies/1', headers=self.EXEC_PRODUCER_HEADER,
            json={
                "title": "Black Swan",
                "release_date": "2010-12-03"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_f_ep_patch_actors(self):
        res = self.client().patch(
            '/actors/1', headers=self.EXEC_PRODUCER_HEADER,
            json={
                "name": "Penelope Cruz",
                "age": 46,
                "gender": "female"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_g_ep_delete_actors(self):
        res = self.client().delete(
            '/actors/1', headers=self.EXEC_PRODUCER_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_h_ep_delete_movies(self):
        res = self.client().delete(
            '/movies/1', headers=self.EXEC_PRODUCER_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

# -----------------------------------------------
# Casting Director Tests
# -----------------------------------------------
    def test_i_cd_get_actor_info(self):
        res = self.client().get(
            '/actors/1', headers=self.CASTING_DIRECTOR_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('actors' in data)

    def test_j_cd_get_movie_info(self):
        res = self.client().get(
            '/movies/1', headers=self.CASTING_DIRECTOR_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('movies' in data)

    def test_k_cd_post_movie(self):
        res = self.client().post(
            '/movies', headers=self.CASTING_DIRECTOR_HEADER,
            json={
                "title": "Black Swan",
                "release_date": "2010-12-03"})
        self.assertNotEqual(res.status_code, 200)

    def test_l_cd_patch_movie(self):
        res = self.client().patch(
            '/movies/1', headers=self.CASTING_DIRECTOR_HEADER,
            json={
                "title": "Fight Club",
                "release_date": "1999-12-03"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_m_cd_post_actors(self):
        res = self.client().post(
            '/actors', headers=self.CASTING_DIRECTOR_HEADER,
            json={
                "name": "Natalie Portman",
                "age": 38,
                "gender": "female"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_n_cd_patch_actors(self):
        res = self.client().patch(
            '/actors/1', headers=self.CASTING_DIRECTOR_HEADER,
            json={
                "name": "Brad Pitt",
                "age": 38,
                "gender": "male"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_o_cd_delete_actors(self):
        res = self.client().delete(
            '/actors/1', headers=self.CASTING_DIRECTOR_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_p_cd_delete_movies(self):
        res = self.client().delete(
            '/movies/1', headers=self.CASTING_DIRECTOR_HEADER)
        self.assertNotEqual(res.status_code, 200)

# -----------------------------------------------
# Casting Assistant Tests
# -----------------------------------------------
    def test_q_ca_get_actor_info(self):
        res = self.client().get(
            '/actors/1', headers=self.CASTING_ASSISTANT_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('actors' in data)

    def test_r_ca_get_movie_info(self):
        res = self.client().get(
            '/movies/1', headers=self.CASTING_ASSISTANT_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('movies' in data)

    def test_s_ca_post_movie(self):
        res = self.client().post(
            '/movies', headers=self.CASTING_ASSISTANT_HEADER,
            json={
                "title": "Black Swan",
                "release_date": "2010-12-03"})
        self.assertNotEqual(res.status_code, 200)

    def test_t_ca_patch_movie(self):
        res = self.client().patch(
            '/movies/1', headers=self.CASTING_ASSISTANT_HEADER,
            json={
                "title": "Fight Club",
                "release_date": "1999-12-03"})
        self.assertNotEqual(res.status_code, 200)

    def test_u_ca_post_actors(self):
        res = self.client().post(
            '/actors', headers=self.CASTING_ASSISTANT_HEADER,
            json={
                "name": "Natalie Portman",
                "age": 38,
                "gender": "female"})
        self.assertNotEqual(res.status_code, 200)

    def test_v_ca_patch_actors(self):
        res = self.client().patch(
            '/actors/1', headers=self.CASTING_ASSISTANT_HEADER,
            json={
                "name": "Brad Pitt",
                "age": 38,
                "gender": "male"})
        self.assertNotEqual(res.status_code, 200)

    def test_w_ca_delete_actors(self):
        res = self.client().delete(
            '/actors/1', headers=self.CASTING_ASSISTANT_HEADER)
        self.assertNotEqual(res.status_code, 200)

    def test_x_ca_delete_movies(self):
        res = self.client().delete(
            '/movies/1', headers=self.CASTING_ASSISTANT_HEADER)
        self.assertNotEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
