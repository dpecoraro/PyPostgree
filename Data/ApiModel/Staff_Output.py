from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class StaffOutput(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    date_of_birth: Optional[datetime]
    gender_ID: Optional[int]
    hire_date: datetime
    position_ID: Optional[int]
    department_ID: Optional[int]
    contact_ID: Optional[int]
    salary: Optional[Decimal]
    staff_status_ID: Optional[int]
    address_ID: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


    class Config:
        orm_mode = True
        allow_population_by_field_name = True