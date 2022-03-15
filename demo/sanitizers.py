from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
import urllib.parse

bp = Blueprint("sanitizers", __name__)


@bp.route("/sanitizers/<name>", methods=["GET", "POST"])
def san(name):
    """Show all the posts, most recent first."""
    # inj = request.args.get("inj")
    if request.method == "POST":
        # inj = request.form['payload']
        # inj = request.args.get("payload")
        data = request.json
        print("data")
        print(data)
        if data:
            inj = data["payload"]
            # inj = request.form['inj']
            inj = urllib.parse.quote(inj, safe="")
            print(inj)
            return inj
            # return redirect("?inj="+inj)
            # print(url_for('san', name=name, inj=inj))
            # return redirect(url_for('san', name=name, inj=inj))
            # return render_template("sanitizers/"+name, inj=inj)
    # if inj:
    #     return render_template("sanitizers/"+name, inj=inj)
    # else:
    return render_template("sanitizers/"+name)



