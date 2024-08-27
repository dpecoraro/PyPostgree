from typing import List, Optional, Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute

from Data.Services.abstract.base_services import BaseService, ModelType

class BaseServiceImpl(BaseService[ModelType]):
    def __init__(self, db_session: AsyncSession, model: Type[ModelType]):
        self.db_session = db_session
        self.model = model
    async def find(self, entity_id: int) -> ModelType:
        query = select(ModelType).where(ModelType.id == entity_id)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def create(self, data: dict) -> ModelType:
        instance = self.model(**data)
        self.db_session.add(instance)
        await self.db_session.commit()
        await self.db_session.refresh(instance)
        return instance

    async def list(self, filters: Optional[dict] = None) -> ModelType:
        query = select(self.model)
        if filters:
            for attr, value in filters.items():
                model_column = getattr(self.model, attr)
                if isinstance(model_column, InstrumentedAttribute):
                    if isinstance(value, bool):
                        query = query.where(model_column.is_(value))
                    else:
                        query = query.where(model_column == value)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def delete(self, entity_id: int) -> None:
        query = select(self.model).where(self.model.id == entity_id)
        result = await self.db_session.execute(query)
        instance = result.scalars().first()
        if instance:
            await self.db_session.delete(instance)
            await self.db_session.commit()

    async def update(self, entity_id: int, data: dict) -> Optional[ModelType]:
        query = select(self.model).where(self.model.id == entity_id)
        result = await self.db_session.execute(query)
        instance = result.scalars().first()
        if instance:
            for key, value in data.items():
                setattr(instance, key, value)
            await self.db_session.commit()
            await self.db_session.refresh(instance)
        return instance

    async def save(self, instance: ModelType) -> ModelType:
        self.db_session.add(instance)
        await self.db_session.commit()
        await self.db_session.refresh(instance)
        return instance

    async def bulk_insert(self, data: List[dict]) -> List[ModelType]:
        instances = [self.model(**item) for item in data]
        self.db_session.add_all(instances)
        await self.db_session.commit()
        return instances