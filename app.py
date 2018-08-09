from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_moment import Moment
from flask_paginate import Pagination, get_page_args
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
pages = FlatPages(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title="Not Found"), 404

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    articles = (p for p in pages if "posts" in p.path)
    articles = (p for p in articles if "draft" not in p.meta)
    latest = sorted(articles, reverse=True, key=lambda p: p.meta['date'])

    # Paginate posts
    tot = len(latest)
    page, per_page, offset = get_page_args()
    articles = latest[offset:offset+per_page]
    pagination = Pagination(page=page,
                            total=tot,
                            record_name="articles",
                            per_page=per_page,
                            show_single_page=True,
                            prev_label="&laquo; ",
                            next_label=" &raquo;")

    return render_template("posts.html",
                           articles=articles,
                           pagination=pagination,
                           title="Posts")

@app.route("/posts/<path:slug>")
def post(slug):
    path = os.path.join("posts", slug)
    page = pages.get_or_404(path)
    return render_template("post.html", page=page)

@app.route("/page/<path:slug>")
def page(slug):
    path = slug
    page = pages.get_or_404(path)
    return render_template("page.html", title=page.meta["title"], page=page)
