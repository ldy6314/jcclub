from flask import Blueprint

studentparent_bp = Blueprint('studentparent', __name__)


@studentparent_bp.route('/')
def studentparent_index():
    return "I am studentparent_index"
