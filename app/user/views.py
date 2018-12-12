from app import app, db
from flask import render_template
from app.auth.models import User

@app.route("/user/<user_id>", methods=["GET"])
def view_profile(user_id):
    user = User.query.get_or_404(user_id)

    if user is None:
        return render_template("user/view.html", user=None)
    return render_template("user/view.html", user=user)