from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

db_session = orm.scoped_session(orm.sessionmaker())