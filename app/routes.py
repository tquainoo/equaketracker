from flask import Blueprint, render_template, request, abort
from .models import Earthquake, Region
from .services.analytics import region_statistics, strongest_earthquakes

main = Blueprint('main', __name__)

@main.route('/')
def index():
    search = request.args.get('search', '')
    query = Earthquake.query

    if search:
        query = query.filter(Earthquake.place.contains(search))

    earthquakes = query.limit(100).all()

    stats = region_statistics()
    strongest = strongest_earthquakes()

    return render_template(
        'dashboard.html',
        earthquakes=earthquakes,
        stats=stats,
        strongest=strongest
    )

@main.route('/earthquake/<int:id>')
def earthquake_detail(id):
    earthquake = Earthquake.query.get(id)

    if not earthquake:
        abort(404)

    related = Earthquake.query.filter_by(
        region_id=earthquake.region_id
    ).limit(5).all()

    return render_template(
        'earthquake_detail.html',
        earthquake=earthquake,
        related=related
    )

@main.route('/region/<int:id>')
def region_detail(id):
    region = Region.query.get(id)

    if not region:
        abort(404)

    return render_template(
        'region_detail.html',
        region=region
    )

@main.app_errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500