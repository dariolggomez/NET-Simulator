from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Sequence
from datetime import datetime

NetNodeBase = declarative_base()
class NetNode(NetNodeBase):
    __tablename__ = 'netNodes'
    id = Column(Integer(), Sequence('rtNode_id_sequence'), primary_key = True)
    nodename = Column(String(25), nullable = False, unique = True)
    city = Column(String(80), nullable = False, unique = False)
    date_created = Column(DateTime(), default = datetime.now)

    def __init__(self, nodename, city):
        self.nodename = nodename
        self.city = city
