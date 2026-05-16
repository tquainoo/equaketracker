from flask import Blueprint, render_template, request, abort
from sqlalchemy import func

from .models import Earthquake, Region
from .services.analytics import region_statistics, strongest_earthquakes
from . import db

main = Blueprint('main', __name__)


# ----------------------------------------------------
# DASHBOARD / HOME
# ----------------------------------------------------
@main.route('/')
def index():

    search = request.args.get('search', '')
    region_id = request.args.get('region', '')
    page = request.args.get('page', 1, type=int)

    PER_PAGE = 20

    query = Earthquake.query

    # Filters
    if search:
        query = query.filter(Earthquake.place.ilike(f"%{search}%"))

    if region_id:
        query = query.filter(Earthquake.region_id == region_id)

    # Pagination
    pagination = query.order_by(Earthquake.id.desc()).paginate(
        page=page,
        per_page=PER_PAGE,
        error_out=False
    )

    earthquakes = pagination.items

    # Analytics
    stats = region_statistics()
    strongest = strongest_earthquakes()

    total_count = Earthquake.query.count()
    max_magnitude = db.session.query(func.max(Earthquake.magnitude)).scalar()
    avg_depth = db.session.query(func.avg(Earthquake.depth)).scalar()
    region_count = Region.query.count()

    regions = Region.query.all()

    return render_template(
        'dashboard.html',
        earthquakes=earthquakes,
        pagination=pagination,
        stats=stats,
        strongest=strongest,
        total_count=total_count,
        max_magnitude=max_magnitude,
        avg_depth=round(avg_depth or 0, 2),
        region_count=region_count,
        regions=regions,
        search=search,
        region_id=region_id
    )


# ----------------------------------------------------
# EARTHQUAKE DETAIL PAGE
# ----------------------------------------------------
@main.route('/earthquake/<int:id>')
def earthquake_detail(id):
    earthquake = Earthquake.query.get_or_404(id)

    related = Earthquake.query.filter(
        Earthquake.region_id == earthquake.region_id,
        Earthquake.id != earthquake.id
    ).limit(10).all()

    return render_template(
        'earthquake_detail.html',
        earthquake=earthquake,
        related=related
    )



# ----------------------------------------------------
# REGION DETAIL PAGE
# ----------------------------------------------------
@main.route('/region/<int:region_id>')
def region_detail(region_id):

    region = Region.query.get_or_404(region_id)

    return render_template(
        'region_detail.html',
        region=region
    )

@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
