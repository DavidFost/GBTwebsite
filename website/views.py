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
