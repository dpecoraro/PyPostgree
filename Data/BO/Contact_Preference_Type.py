from sqlalchemy import Column, Integer, String

from Data.BO.base import Base


class Contact_Preference_Type(Base):
    __tablename__ = 'Contact_Preference_Type'
    contact_preference_type_id = Column(Integer, primary_key=True, autoincrement=True, name='ContactPreferenceTypeID')
    contact_preference_type_name = Column(String, name='ContactPreferenceTypeName')