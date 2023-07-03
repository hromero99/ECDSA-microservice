from sqlalchemy.orm import Session
from src.database.models import KeyModel


def read_key(db: Session, device_id: str):
    return db.query(KeyModel).filter(KeyModel.device_id == device_id).first()


def read_public_key(db: Session, device_id: str):
    data = db.query(KeyModel).filter(KeyModel.device_id == device_id).first()
    if data is not None:
        return data.public_key
    return None


def read_private_key(db: Session, device_id: str):
    data = db.query(KeyModel).filter(KeyModel.device_id == device_id).first()
    if data is not None:
        return data.private_key
    return None
