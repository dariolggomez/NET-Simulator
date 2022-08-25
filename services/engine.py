from models.rtNode_model import RtNodeBase
from models.netNode_model import NetNodeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

connection_string = "postgresql://postgres:simplepass321@localhost/boardDB"
engine = create_engine(connection_string, echo = True)

Session = sessionmaker()

RtNodeBase.metadata.create_all(engine)
NetNodeBase.metadata.create_all(engine)