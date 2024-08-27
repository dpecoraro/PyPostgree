from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List

ModelType = TypeVar('ModelType')
class BaseService(ABC, Generic[ModelType]):
    @abstractmethod
    async def find(self, entity_id: int) -> ModelType:
        pass
    @abstractmethod
    async def create(self, data: dict) -> ModelType:
        pass

    @abstractmethod
    async def list(self, filters: Optional[dict] = None) -> ModelType:
        pass

    @abstractmethod
    async def delete(self, entity_id: int) -> None:
        pass
    @abstractmethod
    async def update(self, entity_id: int, data: dict) -> Optional[ModelType]:
        pass
    @abstractmethod
    async def save(self, instance: ModelType) -> ModelType:
        pass
    @abstractmethod
    async def bulk_insert(self, data: List[dict]) -> List[ModelType]:
        pass
    async def count(self, filters: Optional[dict] = None) -> int:
        return len(await self.list(filters))
    async def exists(self, entity_id: int) -> bool:
        return await self.find(entity_id) is not None