from sqlalchemy.ext.asyncio import AsyncSession

from Data.BO.Addresses import Addresses
from Data.BO.Contacts import Contacts
from Data.BO.Departments import Departments
from Data.BO.Genders import Genders
from Data.BO.Staff import Staff
from Data.Services.base_service_impl import BaseServiceImpl


class AddressServiceImpl(BaseServiceImpl[Addresses]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Addresses)
class ContactServiceImpl(BaseServiceImpl[Contacts]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Contacts)

class DepartmentServiceImpl(BaseServiceImpl[Departments]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Departments)

class StaffServiceImpl(BaseServiceImpl[Staff]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Staff)