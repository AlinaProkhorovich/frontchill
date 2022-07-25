from flask import Blueprint, redirect, render_template, url_for
from events.forms import EventForm, CommentForm


event_blueprint = Blueprint(
    "event",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/event",
)
API = "http://127.0.0.1:8000"


@event_blueprint.route("/add", methods=["GET", "POST"])
def add():
    form = EventForm()
    if form.validate_on_submit():
        form = dict(form.data)
        print(form)
        return redirect(url_for("event"))
    return render_template("event.html", form=form)


# @event_blueprint.route("/comment", methods=["GET", "POST"])
# def comment():
#
