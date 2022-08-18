from .engine import Session, engine
from models.netNode_model import NetNode

local_session = Session(bind = engine)

def create_netNode(nodename, city):
    local_session.add(NetNode(nodename, city))
    local_session.commit()

def read_all():
    netNodes = local_session.query(NetNode).all()
    return netNodes

def read_byID(id):
    netNode = local_session.query(NetNode).filter(NetNode.id == id).first()
    return netNode

def read_byNodename(nodename):
    netNode = local_session.query(NetNode).filter(NetNode.nodename == nodename).first()
    return netNode

def update_netNode(netNode):
    netNode_to_update = read_byID(netNode.id)
    netNode_to_update.nodename = netNode.nodename
    netNode_to_update.city = netNode.city
    local_session.commit()

def delete_netNode(netNode):
    local_session.delete(netNode)
    local_session.commit()