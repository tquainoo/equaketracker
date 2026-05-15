from flask import Blueprint, render_template, request, abort
from sqlalchemy import func

from .models import Earthquake, Region
from .services.analytics import region_statistics, strongest_earthquakes
from . import db

main = Blueprint('main', __name__)


# =========================
# DASHBOARD
# =========================
@main.route('/')
def index():
    search = request.args.get('search', '')
    region_id = request.args.get('region', '')

    query = Earthquake.query

    # Search (PostgreSQL-safe, case-insensitive)
    if search:
        query = query.filter(Earthquake.place.ilike(f"%{search}%"))

    # Region filter
    if region_id:
        query = query.filter(Earthquake.region_id == region_id)

    earthquakes = query.order_by(Earthquake.id.desc()).limit(100).all()

    # Analytics data
    stats = region_statistics()
    strongest = strongest_earthquakes()

    total_count = Earthquake.query.count()

    max_magnitude = db.session.query(
        func.max(Earthquake.magnitude)
    ).scalar()

    avg_depth = db.session.query(
        func.avg(Earthquake.depth)
    ).scalar()

    region_count = Region.query.count()
    regions = Region.query.all()

    return render_template(
        'dashboard.html',
        earthquakes=earthquakes,
        stats=stats,
        strongest=strongest,
        total_count=total_count,
        max_magnitude=max_magnitude,
        avg_depth=round(avg_depth or 0, 2),
        region_count=region_count,
        regions=regions
    )


# =========================
# EARTHQUAKE DETAIL
# =========================
@main.route('/earthquake/<int:id>')
def earthquake_detail(id):
    earthquake = Earthquake.query.get_or_404(id)

    related = Earthquake.query.filter(
        Earthquake.region_id == earthquake.region_id,
        Earthquake.id != earthquake.id
    ).limit(5).all()

    return render_template(
        'earthquake_detail.html',
        earthquake=earthquake,
        related=related
    )


# =========================
# REGION DETAIL
# =========================
@main.route('/region/<int:id>')
def region_detail(id):
    region = Region.query.get_or_404(id)

    return render_template(
        'region_detail.html',
        region=region
    )


# =========================
# ERROR HANDLERS
# =========================
@main.app_errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500