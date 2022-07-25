from datetime import datetime
from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    description: str
    photo: str
    date_event: datetime
    category: str
    place: str
    price: str


class CategoryAdd(BaseModel):
    category: str


class PlaceAdd(BaseModel):
    event: str
    category: int
    place: str
    adress: str


class CommentAdd(BaseModel):
    comment: str
    