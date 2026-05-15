from app.models import Earthquake, Region
from sqlalchemy import func

def region_statistics():
    return (
        Region.query
        .join(Earthquake)
        .with_entities(
            Region.name,
            func.count(Earthquake.id),
            func.avg(Earthquake.magnitude)
        )
        .group_by(Region.name)
        .all()
    )

def strongest_earthquakes(limit=10):
    return (
        Earthquake.query
        .order_by(Earthquake.magnitude.desc())
        .limit(limit)
        .all()
    )