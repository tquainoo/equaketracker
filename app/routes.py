from flask import Blueprint, render_template, request, abort
from sqlalchemy import func

from .models import Earthquake, Region
from .services.analytics import region_statistics, strongest_earthquakes
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():

    # -------------------------
    # QUERY PARAMETERS
    # -------------------------
    search = request.args.get('search', '')
    region_id = request.args.get('region', '')
    page = request.args.get('page', 1, type=int)

    PER_PAGE = 20  # enterprise pagination size

    query = Earthquake.query

    # -------------------------
    # FILTERS
    # -------------------------
    if search:
        query = query.filter(Earthquake.place.ilike(f"%{search}%"))

    if region_id:
        query = query.filter(Earthquake.region_id == region_id)

    # -------------------------
    # PAGINATION (IMPORTANT)
    # -------------------------
    pagination = query.order_by(Earthquake.id.desc()).paginate(
        page=page,
        per_page=PER_PAGE,
        error_out=False
    )

    earthquakes = pagination.items

    # -------------------------
    # ANALYTICS
    # -------------------------
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