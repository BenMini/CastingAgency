from app import app, db, cli
from app.models import Movie, Actor


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Movie': Movie, 'Actor': Actor}
