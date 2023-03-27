def load_config(app):
    try:
        if app.debug:
            print('dev')
            from . import dev
            return dev
        else:
            print('prod')
            from . import prod
            return prod
    except ImportError:
        from . import default
        return default
