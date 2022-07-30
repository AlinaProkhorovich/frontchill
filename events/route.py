from flask import Blueprint, redirect, render_template, url_for, request
from events.forms import EventForm
from events.utils import event_add, photo_add, category_add, place_add
import json
import requests
# from events.aws import upload_file_to_s3
from user.utils import get_current_user

event_blueprint = Blueprint(
    "event",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/event",
)
API = "http://127.0.0.1:8000"


@event_blueprint.route("/add", methods=["POST"])
def add():
    form = EventForm()
    if form.validate_on_submit():
        user = get_current_user()
        user.store_in_session()
        form_data = dict(form.data)

        photo_add(**form_data)
        category_add(**form_data)
        place_add(**form_data)
        return redirect(url_for("home"))
    return render_template("add.html", form=form)




@event_blueprint.route("/list", methods=["GET"])
def post_list():
    articals = requests.get(f"{API}/api/event/").json()
    return render_template("event.html", articals=articals)


