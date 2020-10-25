from sqlalchemy import Column, Integer, String

from app import db


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)