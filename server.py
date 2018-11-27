from datetime import date

from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_parameter
from sqlalchemy_pagination import paginate
from sqlalchemy import or_

from db import db_session, Ad

app = Flask(__name__)

ADS_PER_PAGE = 15

NEW_BUILDING_MAX_AGE = 2


def get_filtered_ads_query(
        oblast_district, min_price, max_price, new_building):
    filtered_ads = db_session.query(Ad).filter(Ad.active)

    if oblast_district:
        filtered_ads = filtered_ads.filter(
            Ad.oblast_district == oblast_district,
        )

    if min_price:
        filtered_ads = filtered_ads.filter(Ad.price >= min_price)

    if max_price:
        filtered_ads = filtered_ads.filter(Ad.price <= max_price)

    if new_building:
        today_year = date.today().year
        filtered_ads = filtered_ads.filter(
            or_(
                Ad.under_construction,
                Ad.construction_year >= today_year - NEW_BUILDING_MAX_AGE,
            ),
        )
    return filtered_ads


@app.route('/')
def ads_list():
    page_number = request.args.get(get_page_parameter(), type=int, default=1)

    filtered_ads_query = get_filtered_ads_query(
        oblast_district=request.args.get('oblast_district'),
        min_price=request.args.get('min_price', type=int),
        max_price=request.args.get('max_price', type=int),
        new_building=request.args.get('new_building', type=bool),
    )
    ads_page = paginate(
        query=filtered_ads_query,
        page=page_number,
        page_size=ADS_PER_PAGE,
    )
    pagination = Pagination(
        page=page_number,
        per_page=ADS_PER_PAGE,
        total=ads_page.total,
        bs_version=3,
    )
    return render_template(
        'ads_list.html',
        ads=ads_page.items,
        pagination=pagination,
    )


if __name__ == "__main__":
    app.run()
