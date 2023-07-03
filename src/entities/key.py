from pydantic import BaseModel


class DeviceKey(BaseModel):
    id: str
    active: bool
