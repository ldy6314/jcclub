from flask import Blueprint

classleader_bp = Blueprint('classleader', __name__)


@classleader_bp.route('/')
def classleader_index():
    return "I am classleader_index"
