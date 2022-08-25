from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

connection_string = "postgresql://postgres:simplepass321@localhost/boardDB"
engine = create_engine(connection_string, echo = True)

Base = declarative_base()
Session = sessionmaker()

def create_all():
    Base.metadata.create_all(engine)