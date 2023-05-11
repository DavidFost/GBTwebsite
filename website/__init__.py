from flask import Flask



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret code'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'GBTpassword'
    app.config['MYSQL_DB'] = 'GBT'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app