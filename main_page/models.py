from sqlalchemy import Column, Integer, Float
from app import db


class SumDb(db.Model):
    __tablename__ = 'sumDb'
    id = Column(Integer(), primary_key=True)
    first_number = Column(Float(), nullable=False)
    second_number = Column(Float(), nullable=False)
    sum = Column(Float())
