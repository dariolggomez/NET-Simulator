from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Sequence
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

NetNodeBase = declarative_base()
class NetNode(NetNodeBase):
    __tablename__ = 'netNodes'
    __id = Column("id", Integer(), Sequence('rtNode_id_sequence'), primary_key = True)
    __nodename = Column("nodename", String(25), nullable = False, unique = True)
    __city = Column("city", String(80), nullable = False, unique = False)
    __date_created = Column("date_created", DateTime(), default = datetime.now)

    def __init__(self, nodename, city):
        self.__nodename = nodename
        self.__city = city
    
    #Hybrid property is used for the private mapping 
    @hybrid_property
    def nodename(self):
        return self.__nodename

    @hybrid_property
    def id(self):
        return self.__id

    @hybrid_property
    def city(self):
        return self.__city
        
    @hybrid_property
    def date_created(self):
        return self.__date_created

    @nodename.setter
    def nodename(self, nodename):
        self.__nodename = nodename

    @city.setter
    def city(self, city):
        self.__city = city