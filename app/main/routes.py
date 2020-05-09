
from flask import request, jsonify, abort
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
@requires_auth('post:actor')
def create_actor(payload):
    try:
        actor = Actor(**request.json)
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
        actor.name = request.json.get['name']
        actor.age = request.json.get['age']
        actor.gender = request.json.get['gender']
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
        movie = Movie(**request.json)
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
        movie.title = request.json['title']
        movie.release_date = request.json['release_date']
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
