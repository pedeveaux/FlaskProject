from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_user

bp = Blueprint(
    "auth_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="assets",
)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    return render_template("auth/login.html")


@bp.route("/register.html")
def register():
    return render_template("auth/register.html")
