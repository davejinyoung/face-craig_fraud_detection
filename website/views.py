from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("base.html", text="TESTING")


@views.route('/fb')
def face():
    return render_template("face.html", text="TESTING")


@views.route('/craig')
def craig():
    return render_template("craig.html", text="TESTING")


@views.route('/about')
def about():
    return render_template("about.html", text="TESTING")
