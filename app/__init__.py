import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'earthquake-secret'
    
    database_url = "postgresql://earthquake_db_rhjn_user:1BCTa1hw4T5M0pqIZerbQDXUQsLwhAOf@dpg-d83klujeo5us73bcp9b0-a.ohio-postgres.render.com:5432/earthquake_db_rhjn"

    # FIX 2: FORCE SSL (CRITICAL for Render)
    if "postgresql://" in database_url:
        database_url += "?sslmode=require"


    # FIX 3: production-safe pool settings
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        "pool_pre_ping": True,
        "pool_recycle": 280
    }

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app