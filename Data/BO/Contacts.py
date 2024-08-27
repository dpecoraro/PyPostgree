from sqlalchemy import Column, Integer, ForeignKey, String

from Data.BO.base import Base


class Contacts(Base):
    __tablename__ = 'Contacts'
    id = Column(Integer, primary_key=True, name='ContactID')
    contact_type_preference_id = Column(Integer,
                                        ForeignKey('Contact_Preference_Type.ContactPreferenceTypeID',
                                                   name='FK_Contacts_Contacts_Preference_Type'),)
    email = Column(String, unique=True, name='Email')
    phone_number = Column(String, name='PhoneNumber')
    fax_number = Column(String, name='FaxNumber')