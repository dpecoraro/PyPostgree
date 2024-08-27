from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from Data.ApiModel.Staff_Output import StaffOutput
from Data.BO.Staff import Staff
from Data.Services.hospital_services import StaffServiceImpl
from Data.Services.service_factory import get_service

router = APIRouter()
staff_service_factory = get_service(StaffServiceImpl)
@router.get("/staff", response_model=List[StaffOutput])
async def get_staffs(staff_service: StaffServiceImpl = Depends(staff_service_factory)):
    response = await staff_service.list()
    return response

@router.post("/staff", response_model=StaffOutput, status_code=status.HTTP_201_CREATED)
async def save_staff(staff: StaffOutput, staff_service: StaffServiceImpl = Depends(staff_service_factory)):
    dto = build_staff(staff)
    response = await staff_service.save(dto)
    return response


def build_staff(inputModel: StaffOutput) -> Staff:
    data = Staff()
    data.staff_status_ID = inputModel.staff_status_ID if inputModel.staff_status_ID else None
    data.salary = inputModel.salary
    data.id = inputModel.id if inputModel.id else None
    data.gender_ID = inputModel.gender_ID
    data.address_ID = inputModel.address_ID
    data.created_at = inputModel.created_at
    data.updated_at = inputModel.updated_at if inputModel.updated_at else None
    data.date_of_birth = inputModel.date_of_birth
    data.department_ID = inputModel.department_ID
    data.last_name = inputModel.last_name
    data.first_name = inputModel.first_name
    data.hire_date = inputModel.hire_date
    return data
