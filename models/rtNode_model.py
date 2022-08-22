from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Sequence
from datetime import datetime

Base = declarative_base()
class RtNode(Base):
    __tablename__='rtNodes'
    __id = Column(Integer(), Sequence('rtNode_id_sequence'), primary_key = True)
    __nodename = Column(String(25), nullable = False, unique = True)
    __city = Column(String(80), nullable = False, unique = False)
    __date_created = Column(DateTime(), default = datetime.now)

    def __ini__(self, nodename, city):
        self.__nodename = nodename
        self.__city = city

    def getId(self):
        return self.__id

    def getNodename(self):
        return self.__nodename

    def getCity(self):
        return self.__city

    def getDatecreated(self):
        return self.__date_created

    def setNodename(self, nodename):
        self.__nodename = nodename

    def setCity(self, city):
        self.__city = city
