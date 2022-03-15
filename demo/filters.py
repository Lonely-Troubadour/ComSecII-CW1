from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

bp = Blueprint("filters", __name__)


@bp.route("/filters/<name>", methods=["GET", "POST"])
def filter(name):
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
        return render_template("filters/"+name, inj=inj)
    else:
        return render_template("filters/"+name, name=name)


