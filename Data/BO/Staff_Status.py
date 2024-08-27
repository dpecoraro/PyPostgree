from sqlalchemy import Column, Integer, String

from Data.BO.base import Base


class Staff_Status(Base):
    __tablename__ = 'Staff_Status'
    id = Column(Integer, primary_key=True, autoincrement=True, name='Staff_StatusID')
    name = Column(String)