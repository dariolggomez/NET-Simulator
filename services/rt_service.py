from .engine import Session, engine
from models.rtNode_model import RtNode

local_session = Session(bind = engine)

def create_rtNode(nodename, city):
    local_session.add(RtNode(nodename, city))
    local_session.commit()

def read_all():
    rtNodes = local_session.query(RtNode).all()
    return rtNodes

def read_byID(id):
    rtNode = local_session.query(RtNode).filter(RtNode.id == id).first()
    return rtNode

def read_byNodename(nodename):
    rtNode = local_session.query(RtNode).filter(RtNode.nodename == nodename).first()
    return rtNode

def update_RtNode(rtNode):
    rtNode_to_update = read_byID(rtNode.id)
    rtNode_to_update.nodename = rtNode.nodename
    rtNode_to_update.city = rtNode.city
    local_session.commit()

def delete_rtNode(rtNode):
    local_session.delete(rtNode)
    local_session.commit()