from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
import urllib.parse

bp = Blueprint("csp", __name__)


@bp.route("/csp/<name>", methods=["GET", "POST"])
def csp(name):
    """Show all the posts, most recent first."""
    if request.method == "POST":
        data = request.json
        if data:
            inj = data["payload"]
            # inj = request.form['inj']
            inj = urllib.parse.quote(inj, safe="")
            print(inj)
            return inj
    inj = request.args.get("inj")
    if inj:
        return render_template("csp/"+name, inj=inj)
    else:
        return render_template("csp/"+name, name=name)

@bp.route("/csp/attack/<name>", methods=["GET", "POST"])
def csp_attack(name):
    """Show all the posts, most recent first."""
    if request.method == "POST":
        data = request.json
        if data:
            inj = data["payload"]
            # inj = request.form['inj']
            inj = urllib.parse.quote(inj, safe="")
            print(inj)
            return inj
    inj = request.args.get("inj")
    if inj:
        return render_template("csp/angularjs-ue-exploit.html", inj=inj)
    else:
        return render_template("csp/angularjs-ue-exploit.html", name=name)

@bp.route("/csp/nonce/<name>", methods=["GET", "POST"])
def csp_nonce(name):
    """Show all the posts, most recent first."""
    if request.method == "POST":
        data = request.json
        
        if data:
            inj = data["payload"]
            # inj = request.form['inj']
            inj = urllib.parse.quote(inj, safe="")
            print(inj)
            return inj
    inj = request.args.get("inj")
    if inj:
        return render_template("csp/nonce-exploit.html", inj=inj)
    else:
        return render_template("csp/nonce-exploit.html", name=name)
