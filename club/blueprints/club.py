from flask import Blueprint

club_bp = Blueprint('base', __name__)


@club_bp.route('/')
def index():
    return "I am base"
