
from flask import request, jsonify, abort, json
from app.models import Movie, Actor
from app.auth.auth import requires_auth
from app.main import bp


@bp.route('/')
def index():
    return jsonify({
        'hello': 'Hello World'
    })

# --------------------------------------------------------
# ACTORS ROUTES
# --------------------------------------------------------
@bp.route('/actors', methods=['GET'])
def get_actors():
    try:
        return jsonify({
            'success': True,
            'actors': [actor.short() for actor in Actor.query.all()]
        }), 200

    except Exception as e:
        print(e)
        abort(404)


@bp.route('/actors', methods=['POST'])
# @requires_auth('post:actor')
def create_actor():
    try:
        actor = Actor(
            name=json.dumps(request.json['name']),
            age=json.dumps(request.json['age']),
            gender=json.dumps(request.json['gender'])
        )
        actor.insert()
        return jsonify({
            'success': True,
            'actors': [actor.long()]
        }), 200

    except Exception as e:
        print(e)
        abort(422)


@bp.route('/actors/<actor_id>', methods=['GET'])
@requires_auth('get:actor-info')
def get_actor_info(payload, actor_id):
    try:
        actor = Actor.query.filter(Actor.id == actor_id).first()
        return jsonify({
            'success': True,
            'actors': [actor.long()]
        }), 200
    except Exception as e:
        print(e)
        abort(404)


@bp.route('/actors/<actor_id>', methods=['PATCH'])
@requires_auth('patch:actor')
def update_actor(payload, actor_id):
    try:
        actor = Actor.query.filter(Actor.id == actor_id).first()
        actor.name = json.dumps(request.json.get('name'), None)
        actor.age = json.dumps(request.json.get('age'), None)
        actor.gender = json.dumps(request.json.get('gender'), None)
        actor.update()
        return jsonify({
            'success': True,
            'actors': [actor.long()]
        }), 200
    except Exception as e:
        print(e)
        abort(404)


@bp.route('/actors/<actor_id>', methods=['DELETE'])
@requires_auth('delete:actor')
def delete_actor(payload, actor_id):
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

# --------------------------------------------------------
# MOVIES ROUTES
# --------------------------------------------------------
@bp.route('/movies', methods=['GET'])
def get_movies():
    try:
        return jsonify({
            'success': True,
            'movies': [movie.short() for movie in Movie.query.all()]
        }), 200

    except Exception as e:
        print(e)
        abort(404)


@bp.route('/movies', methods=['POST'])
@requires_auth('post:movie')
def create_movie(payload):
    try:
        movie = Movie(
            title=json.dumps(request.json['title']),
            release_date=json.dumps(request.json['release_date'])
        )
        movie.insert()
        return jsonify({
            'success': True,
            'movies': [movie.short()]
        }), 200
    except Exception as e:
        print(e)
        abort(401)


@bp.route('/movies/<movie_id>', methods=['GET'])
@requires_auth('get:movie-info')
def get_movie_info(payload, movie_id):
    try:
        movie = Movie.query.filter(Movie.id == movie_id).first()
        return jsonify({
            'success': True,
            'movies': [movie.long()]
        }), 200
    except Exception as e:
        print(e)
        abort(404)


@bp.route('/movies/<movie_id>', methods=['PATCH'])
@requires_auth('patch:movie')
def update_movie(payload, movie_id):
    try:
        movie = Movie.query.filter(Movie.id == movie_id).first()
        movie.title = json.dumps(request.json['title'])
        movie.release_date = json.dumps(request.json['release_date'])
        movie.update()
        return jsonify({
            'success': True,
            'movies': [movie.long()]
        }), 200
    except Exception as e:
        print(e)
        abort(401)


@bp.route('/movies/<movie_id>', methods=['DELETE'])
@requires_auth('delete:movie')
def delete_movie(payload, movie_id):
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
