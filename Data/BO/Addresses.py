from sqlalchemy import Column, Integer, String

from Data.BO.base import Base


class Addresses(Base):
    __tablename__ = 'Addresses'
    id = Column(Integer, primary_key=True, autoincrement=True, name='AddressID')
    street_address = Column(String, nullable=False, name='StreetAddress')
    city = Column(String, nullable=False, name='City')
    state = Column(String, nullable=False, name='State')
    zip_code = Column(String, nullable=False, name='ZipCode')
    country = Column(String, nullable=False, name='Country')
