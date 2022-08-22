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
    rtNode = local_session.query(RtNode).filter(RtNode.getId() == id).first()
    return rtNode

def read_byNodename(nodename):
    rtNode = local_session.query(RtNode).filter(RtNode.getNodename() == nodename).first()
    return rtNode

def update_RtNode(rtNode):
    rtNode_to_update = read_byID(rtNode.getId())
    rtNode_to_update.setNodename(rtNode.getNodename())
    rtNode_to_update.setCity(rtNode.getCity())
    local_session.commit()

def delete_rtNode(rtNode):
    local_session.delete(rtNode)
    local_session.commit()