from services import engine
from models.rtNode_model import RtNode
from sqlalchemy import exists

local_session = engine.Session(bind = engine.engine)
engine.create_all()

def create_rtNode(nodename, city, net_id):
    local_session.add(RtNode(nodename, city, net_id))
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
    rtNode_to_update.nodename(rtNode.nodename)
    rtNode_to_update.city(rtNode.city)
    local_session.commit()

def delete_rtNode(rtNode):
    local_session.delete(rtNode)
    local_session.commit()

def checkNodenameExists(nodename):
    ret = local_session.query(exists().where(RtNode.nodename == nodename)).scalar()
    return ret