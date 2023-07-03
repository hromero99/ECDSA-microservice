from src.entities import DeviceKey
from src.database.models import KeyModel


def create_key(db, key_model=DeviceKey):
    db_key = KeyModel(
        device_id=key_model.device_id,
        public_key=key_model.pub_key,
        private_key=key_model.priv_key,
    )
    db.add(db_key)
    db.commit()
    db.refresh(db_key)
    return db_key
