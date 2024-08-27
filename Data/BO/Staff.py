from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, DECIMAL

from Data.BO.base import Base


class Staff(Base):
    __tablename__ = 'Staff'
    id = Column(Integer, primary_key=True, autoincrement=True, name='StaffID')
    first_name = Column(String, nullable=False, name='FirstName')
    last_name = Column(String, nullable=False, name='LastName')
    date_of_birth = Column(DateTime, name='DateOfBirth')
    gender_ID = Column(Integer, ForeignKey('Genders.GenderID', name='FK_Staff_Gender'))
    hire_date = Column(DateTime, nullable=False, name='HireDate')
    position_ID = Column(Integer, ForeignKey('Positions.PositionID', name='FK_Staff_Position'))
    department_ID = Column(Integer, ForeignKey('Departments.DepartmentID', name='FK_Staff_Department'))
    contact_ID = Column(Integer, ForeignKey('Contacts.ContactID', name='FK_Staff_Contact'))
    salary = Column(DECIMAL, name='Salary')
    staff_status_ID = Column(Integer, ForeignKey('Staff_Status.Staff_StatusID', name='FK_Staff_StaffStatus'))
    address_ID = Column(Integer, ForeignKey('Addresses.AddressID', name='FK_Staff_Address'))
    created_at = Column(DateTime, default=datetime.now, name='CreatedAt')
    updated_at = Column(DateTime, name='UpdatedAt')
