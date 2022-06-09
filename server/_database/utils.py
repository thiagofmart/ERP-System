from .database import Base, engine_write_instance, engine_read_instance, Session_write, Session_read
from . import models
from sqlalchemy_utils import database_exists

def _create_database():
    Base.metadata.create_all(engine_write_instance)
    Base.metadata.create_all(engine_read_instance)


async def get_db_write():
    db = Session_write()
    try:
        yield db
    finally:
        db.close()

async def get_db_read():
    db = Session_read()
    try:
        yield db
    finally:
        db.close()
