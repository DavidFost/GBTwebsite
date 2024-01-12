from flask import Blueprint, render_template, session, g, redirect, request, flash, url_for
from flask_login import login_required, current_user
import mysql.connector
import datetime


views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("homepage.html")


@views.route('/watch', methods = ['GET', 'POST'])
def watch():
    return render_template("watch.html")


@views.route('/about-us')
def about():
    return render_template("about-us.html")

@views.route('/give')
def give():
    return render_template("give.html")


@views.route('/connect')
def connect():
    return render_template("connect.html")


@views.route('/events')
def events():
    return render_template("events.html")


@views.route('/youth')
def youth():
    return render_template("youth.html")

@views.route('/childrens_ministry')
def childrens_ministry():
    return render_template("childrens_ministry.html")

@views.route('/arts')
def arts():
    return render_template("music-finearts.html")

@views.route('/sundayschool')
def sundayschool():
    return render_template("sundayschool.html")

@views.route('/missions')
def missions():
    return render_template("missions.html")

@views.route('/education')
def education():
    return render_template("education.html")

@views.route('/aberdeen')
def aberdeen():
    return render_template("aberdeen.html")

@views.route('/evangelism')
def evangelism():
    return render_template("evangelism-outreach.html")

@views.route('/first-lady')
def first():
    return render_template("first-lady.html")

@views.route('/what-to-expect')
def expect():
    return render_template("what-to-expect.html")

@views.route('/pastor')
def pastor():
    return render_template("our-pastor.html")

@views.route('/belief')
def belief():
    return render_template("our-belief.html")
