from sqlalchemy import Column, Integer, String

from Data.BO.base import Base


class Departments(Base):
    __tablename__ = 'Departments'
    id = Column(Integer, primary_key=True, autoincrement=True, name='DepartmentID')
    name = Column(String, name='DepartmentName')