from app import app
from flask import render_template


@app.route("/")
def show_feed_list():
    return render_template('feed_list.html')


@app.route("/feed/<int:feed_id>")
def show_post_list(feed_id):
    return render_template('post_list.html')
