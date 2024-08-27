from sqlalchemy import Column, Integer, String

from Data.BO.base import Base


class Positions(Base):
    __tablename__ = 'Positions'
    id = Column(Integer, primary_key=True, autoincrement=True, name='PositionID')
    name = Column(String, nullable=False)