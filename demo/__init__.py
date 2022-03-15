import os
import urllib.parse
from flask import Flask, render_template, request
import random


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Add url encode and random functions
    def encodeurl(url):
        return urllib.parse.quote(url, safe="")
    app.jinja_env.globals.update(encodeurl=encodeurl)

    def gen_random():
        return random.randint(1, 65535)
    app.jinja_env.globals.update(gen_random=gen_random)

    # Blueprints
    from demo import csp, filters, sanitizers

    app.register_blueprint(csp.bp)
    app.register_blueprint(filters.bp)
    app.register_blueprint(sanitizers.bp)

    @app.route("/hello")
    def hello():
        return "Hello, World!"
    
    @app.route("/")
    def home():
        return render_template("home.html")
    
    @app.route("/test", methods=["GET", "POST"])
    def test():
        if request.method == "GET":
            inj = request.args.get("inj")
            return render_template("vue.html", inj=inj)
        return render_template("vue.html")

    # register the database commands
    # from flaskr import db

    # db.init_app(app)

    # apply the blueprints to the app
    # from flaskr import auth, blog

    # app.register_blueprint(auth.bp)
    # app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app