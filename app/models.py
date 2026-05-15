from . import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    regions = db.relationship('Region', backref='country', lazy=True)

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    earthquakes = db.relationship('Earthquake', backref='region', lazy=True)

class Earthquake(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    quake_id = db.Column(db.String(50), unique=True)
    magnitude = db.Column(db.Float)
    depth = db.Column(db.Float)
    place = db.Column(db.String(255))
    event_time = db.Column(db.String(100))
    tsunami = db.Column(db.Integer)

    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))