import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS


@app.route('/actors', methods=['GET', 'POST'])
def get_actors():
    if request.method == 'GET':
        def show_actors():
            try:
                return jsonify({
                    'success': True,
                    'actors': [actor.short() for actor in Actor.query.all()]
                }), 200

            except Exception as e:
                print(e)
                abort(404)

    if request.method == 'POST':
        def create_actor():
            try:
                actor = Actor(
                    name=request.json.get('name')
                )
                actor.insert()
                return jsonify({
                    'success': True,
                    'actor': [actor.short()]
                }), 200
            except Exception as e:
                print(e)
                abort(422)


@app.route('/actors/<actor_id>', methods=['GET', 'PATCH', 'DELETE'])
def actor_info(actor_id):
    if request.method == 'GET':
        def get_actor_info(actor_id):
            try:
                actor = Actor.query.filter(Actor.id == actor_id).first()
                return jsonify({
                    'success': True,
                    'actor': [actor.long()]
                }), 200
            except Exception as e:
                print(e)
                abort(404)

    if request.method == 'PATCH':
        def update_actor(actor_id):
            try:
                actor = Actor.query.filter(Actor.id == actor_id).first()
                actor.name = request.json.get('name')
                actor.update()
                return jsonify({
                    'success': True,
                    'actor': [actor.long()]
                }), 200
            except Exception as e:
                print(e)
                abort(404)

    if request.method == 'DELETE':
        def delete_actor(actor_id):
            try:
                actor = Actor.query.filter(Actor.id == actor_id).first()
                actor.delete()
                return jsonify({
                    'success': True,
                    'delete': actor.id
                }), 200
            except Exception as e:
                print(e)
                abort(404)


@app.route('/movies', methods=['GET', 'POST'])
def get_movies():
    if request.method == 'GET':
        def show_movies():
            try:
                return jsonify({
                    'success': True,
                    'movies': [movie.short() for movie in Movie.query.all()]
                }), 200

            except Exception as e:
                print(e)
                abort(404)

    if request.method == 'POST':
        def create_movie():
            try:
                movie = Movie(
                    name=request.json.get('name')
                )
                movie.insert()
                return jsonify({
                    'success': True,
                    'movies': [movie.short()]
                }), 200
            except Exception as e:
                print(e)
                abort(401)


@app.route('/movies/<movie_id>', methods=['PATCH', 'DELETE'])
def movie_info(movie_id):
    if request.method == 'GET':
        def get_movie_info(movie_id):
            try:
                movie = Movie.query.filter(Movie.id == movie_id).first()
                return jsonify({
                    'success': True,
                    'movies': [movie.long()]
                }), 200
            except Exception as e:
                print(e)
                abort(404)

    if request.method == 'PATCH':
        def update_movie(movie_id):
            try:
                movie = Movie.query.filter(Movie.id == movie_id).first()
                movie.name = requst.json.get('name')
                movie.update()
                return jsonify({
                    'success': True,
                    'movies': [movie.long()]
                }), 200
            except Exception as e:
                print(e)
                abort(401)

    if request.method == 'DELETE':
        def delete_movie(movie_id):
            try:
                movie = Movie.query.filter(Movie.id == movie_id).first()
                movie.delete()
                return jsonify({
                    'success': True,
                    'delete': movie.id
                }), 200
            except Exception as e:
                print(e)
                abort(404)
