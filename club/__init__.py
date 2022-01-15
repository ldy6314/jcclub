from flask import Flask
from club.blueprints.admin import admin_bp
from club.blueprints.studentparent import studentparent_bp
from club.blueprints.classleader import classleader_bp
from club.blueprints.club import club_bp


def create_app(config_name=None):
    if not config_name:
        pass
    app = Flask('club')
    app.register_blueprint(club_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(classleader_bp, url_prefix='/classleader')
    app.register_blueprint(studentparent_bp, url_prefix='/studentparent')
    return app


if __name__ == '__main__':
    app1 = create_app()
    app1.run()