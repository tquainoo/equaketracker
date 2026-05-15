from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'earthquake-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        "DATABASE_URL",
        "sqlite:////tmp/earthquake.db"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print("DB init error:", e)

    return app