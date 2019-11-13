from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config["SECRET_KEY"] = 'supersecret'

posts = [
    {
        'auteur': 'Hans Beijk',
        'titel': 'Blog post 1',
        'content': 'Eerste blog post van Hans',
        'datum': '11 November, 2019'
    },
    {
        'auteur': 'Toos Peskens',
        'titel': 'Blog post 2',
        'content': 'Eerste blog post van Toos',
        'datum': '9 November, 2019'
    },
]


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


if __name__ == "__main__":
    app.run(debug=True)
