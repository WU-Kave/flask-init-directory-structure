from flask import Flask
import config


def create_app():
    print('create app')
    app = Flask(__name__)
    myconfig = config.load_config(app)
    app.config.from_object(myconfig)
    from . import models, routes, services
    models.init_app(app)
    routes.init_app(app)
    services.init_app(app)
    return app
