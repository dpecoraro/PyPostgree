from Data.BO.Addresses import Addresses
from Data.BO.Contact_Preference_Type import Contact_Preference_Type
from Data.BO.Contacts import Contacts
from Data.BO.Departments import Departments
from Data.BO.Genders import Genders
from Data.BO.Positions import Positions
from Data.BO.Staff import Staff
from Data.BO.Staff_Status import Staff_Status


table_creation_order = [
    Staff_Status.__table__,
    Positions.__table__,
    Genders.__table__,
    Contact_Preference_Type.__table__,
    Departments.__table__,
    Contacts.__table__,
    Addresses.__table__,
    Staff.__table__,
]