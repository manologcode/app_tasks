from flask import Flask
from flask_migrate import Migrate
from app.config import config_by_name
from app.models import db

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    Migrate(app, db)
    
    # Register blueprints
    from app.routes.project_routes import project_bp
    from app.routes.tag_routes import tag_bp
    from app.routes.task_routes import task_bp
    app.register_blueprint(project_bp)
    app.register_blueprint(tag_bp)
    app.register_blueprint(task_bp)

    return app
