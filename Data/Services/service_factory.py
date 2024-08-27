from typing import TypeVar, Type

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from Data.Services.abstract.base_services import BaseService
from Infra.database_conn import get_db

ModelType = TypeVar("ModelType")

def get_service(service_class: Type[BaseService[ModelType]]):
    async def _get_service(db: AsyncSession = Depends(get_db)) -> BaseService[ModelType]:
        return service_class(db)
    return _get_service