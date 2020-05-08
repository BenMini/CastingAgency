from flask import jsonify
from app.errors import bp
from app.auth.auth import AuthError


@bp.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400


@bp.errorhandler(401)
def unauthorized(error):
    '''Error handling for Unauthorized Access'''
    return jsonify({
        'success': False,
        'error': 401,
        'message': 'Unauthorized'
    }), 401


@bp.errorhandler(403)
def forbidden(error):
    '''Error handling for Authentication Error'''
    return jsonify({
        'success': False,
        'error': 403,
        'message:': 'Forbidden Authentication Error'
    }), 403


@bp.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource Not Found"
    }), 404


@bp.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Not Processable"
    }), 422


@bp.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error"
    }), 500


@bp.errorhandler(AuthError)
def auth_error(error):
    '''Error handling for Authorization Error'''
    return jsonify({
        'success': False,
        'error': error.status_code,
        'message': error.error
    }), error.status_code
