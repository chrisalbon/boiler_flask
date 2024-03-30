from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
dbootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # flashes if new name submitted does not match previous name
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")
        session["name"] = form.name.data
        return redirect(url_for("index"))
    return render_template("index.html", form=form, name=session.get("name"))
