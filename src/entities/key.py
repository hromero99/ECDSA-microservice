from pydantic import BaseModel


class DeviceKey(BaseModel):
    device_id: str
    priv_key: bytes
    pub_key: bytes
