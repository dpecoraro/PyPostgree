from sqlalchemy import Column, Integer, String
from Data.BO.base import Base

class Genders(Base):
    __tablename__ = 'Genders'
    id = Column(Integer, primary_key=True, autoincrement=True ,name='GenderID')
    name = Column(String, name='Name')