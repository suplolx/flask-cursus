from flask import render_template, url_for, flash, redirect

from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@kr8tig.nl' and form.password.data == "Welkom01":
            flash("You have been logged in successfully", category="success")
            return redirect(url_for('index'))
        else:
            flash("Login unsuccessful. Please check username and password", category="danger")
    return render_template("login.html", title="Login", form=form)