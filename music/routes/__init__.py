from .auth_routes import blp as AuthBlp
from .music_routes import blp as MusicBlp


def register_blueprints(app):
    app.register_blueprint(AuthBlp)
    app.register_blueprint(MusicBlp)
