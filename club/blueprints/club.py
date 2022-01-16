from flask import Blueprint, render_template

club_bp = Blueprint('base', __name__)


@club_bp.route('/')
def index():
    return render_template("base.html")
