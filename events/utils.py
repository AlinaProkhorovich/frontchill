

import requests
from config import Config
from events.models import Event, PlaceAdd, CommentAdd, CategoryAdd


CREATE_EVENT = f"{Config.API_URL}/api/event/"
CREATE_PLACE = f"{Config.API_URL}/api/place/"
CREATE_CATEGORY = f"{Config.API_URL}/api/place/"
CREATE_COMMENT = f"{Config.API_URL}/comment/"


def event_add(*args, **kwargs)-> Event:
    event_add = Event(**kwargs)
    res = requests.post(CREATE_EVENT, json=event_add.dict())
    event = Event(**res.json())
    return event

def comment_add(*args, **kwargs) -> CommentAdd:
    comment_add = CommentAdd(**kwargs)
    res = requests.post(CREATE_COMMENT, json=comment_add.dict())
    comment = CommentAdd(**res.json())
    return comment


def place_add(*args, **kwargs) -> PlaceAdd:
    place_add = PlaceAdd(**kwargs)
    res = requests.post(CREATE_PLACE, json=place_add.dict())
    place = CommentAdd(**res.json())
    return place

def category_add(*args, **kwargs) -> CategoryAdd:
    category_add = CategoryAdd(**kwargs)
    res = requests.post(CREATE_CATEGORY, json=category_add.dict())
    category = CategoryAdd(**res.json())
    return category