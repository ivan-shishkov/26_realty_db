from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_parameter
from sqlalchemy_pagination import paginate

from db import db_session, Ad

app = Flask(__name__)

ADS_PER_PAGE = 15


@app.route('/')
def ads_list():
    page = request.args.get(get_page_parameter(), type=int, default=1)

    ads_page = paginate(
        query=db_session.query(Ad).filter(Ad.active),
        page=page,
        page_size=ADS_PER_PAGE,
    )
    pagination = Pagination(
        page=page,
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
