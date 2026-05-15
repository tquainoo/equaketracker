from app import create_app, db
from app.models import Country, Region, Earthquake
import random

app = create_app()

countries = ['USA', 'Japan', 'Chile', 'Indonesia']
regions = ['California', 'Tokyo', 'Santiago', 'Jakarta']

with app.app_context():

    db.drop_all()
    db.create_all()

    country_objs = {}

    for country in countries:
        c = Country(name=country)
        db.session.add(c)
        db.session.commit()
        country_objs[country] = c

    region_objs = {}

    for i, region in enumerate(regions):
        r = Region(
            name=region,
            country_id=country_objs[countries[i]].id
        )
        db.session.add(r)
        db.session.commit()
        region_objs[region] = r

    for i in range(5000):

        region = random.choice(regions)

        quake = Earthquake(
            quake_id=f'EQ-{100000+i}',
            magnitude=round(random.uniform(1.0, 9.0), 1),
            depth=round(random.uniform(1, 700), 1),
            place=f'Zone {i}',
            event_time='2026-01-01',
            tsunami=random.randint(0,1),
            region_id=region_objs[region].id
        )

        db.session.add(quake)

    db.session.commit()

    print('Database seeded successfully.')