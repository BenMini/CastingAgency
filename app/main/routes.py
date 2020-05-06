
from flask import request, jsonify, abort
from app.models import Movie, Actor
from app.auth.auth import AuthError, requires_auth
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
def create_actor():
    body = request.get_json()
    try:
        actor = Actor(
            name=body.get('name'),
            age=body.get('age'),
            gender=body.get('gender')
        )
        actor.insert()
        return jsonify({
            'success': True,
            'actors': [actor.short()]
        }), 200

    except Exception as e:
        print(e)
        abort(422)


@bp.route('/actors/<actor_id>', methods=['GET'])
def get_actor_info(actor_id):
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
def update_actor(actor_id):
    try:
        actor = Actor.query.filter(Actor.id == actor_id).first()
        actor.name = request.json.get('name')
        actor.age = request.json.get('age')
        actor.gender = request.json.get('gender')
        actor.update()
        return jsonify({
            'success': True,
            'actors': [actor.long()]
        }), 200
    except Exception as e:
        print(e)
        abort(404)


@bp.route('/actors/<actor_id>', methods=['DELETE'])
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
def create_movie():
    try:
        movie = Movie(
            title=request.json['title'],
            release_date=request.json['release_date'].date()
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

        return get_movie_info()


@bp.route('/movies/<movie_id>', methods=['PATCH'])
def update_movie(movie_id):
    try:
        movie = Movie.query.filter(Movie.id == movie_id).first()
        movie.name = request.json.get('name')
        movie.update()
        return jsonify({
            'success': True,
            'movies': [movie.long()]
        }), 200
    except Exception as e:
        print(e)
        abort(401)


@bp.route('/movies/<movie_id>', methods=['DELETE'])
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
