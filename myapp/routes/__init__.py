from .home import root_bp


def init_app(app):
    app.register_blueprint(root_bp)
