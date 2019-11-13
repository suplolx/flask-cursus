from flask import Flask, render_template, url_for
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


if __name__ == "__main__":
    app.run(debug=True)
