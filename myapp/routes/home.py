from flask import Blueprint, jsonify
root_bp = Blueprint('root_bp', __name__, url_prefix='/')


@root_bp.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@root_bp.route('/test1', methods=['GET', 'POST'])
def test1():
    return jsonify({
        "code": 200,
        "msg": "test1 success",
        "data": None
    })
