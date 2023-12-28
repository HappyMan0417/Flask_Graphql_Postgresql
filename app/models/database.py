from app.models import Base, db_session
from sqlalchemy import create_engine
from app.models.user_model import ExampleModel

def init_database(uri):
    engine = create_engine(uri, echo=True)

    Base.metadata.create_all(bind=engine)
    db_session.configure(bind=engine)