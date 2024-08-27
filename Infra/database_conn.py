from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/hospitalDB"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine, class_=AsyncSession)

async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            session.close()