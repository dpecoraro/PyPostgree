from sqlalchemy import inspect

from Data.BO.base import Base
from Infra.table_seq_order import table_creation_order


async def drop_tables(conn):
    await conn.run_sync(Base.metadata.drop_all)

async def create_tables(conn):
    for table in table_creation_order:
        await conn.run_sync(table.create)

async def check_tables_exist(conn):
    def sync_inspect(connection):
        inspector = inspect(connection)
        return inspector.get_table_names()

    tables = await conn.run_sync(sync_inspect)
    return tables

async def recreate_tables(engine):
    try:
        async with engine.begin() as conn:
            tables = await check_tables_exist(conn)
            if tables:
                await drop_tables(conn)
            tables = await check_tables_exist(conn)
            await create_tables(conn)
    except Exception as e:
        print(e)


async def validate_startup_job(conn):
    result = await conn.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = result.scalars().all()
    return tables

