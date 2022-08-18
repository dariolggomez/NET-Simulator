from curses import echo
from models.rtNode_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

connection_string = "postgresql://postgres:simplepass321@localhost/boardDB"
engine = create_engine(connection_string, echo = True)

Session = sessionmaker()

Base.metadata.create_all(engine)