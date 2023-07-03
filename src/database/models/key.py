from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from database import Base


class KeyModel(Base):
    __tablename__ = "keys"
    device_id = Column(String, primary_key=True, index=True)
    public_key = Column(LargeBinary)
    private_key = Column(LargeBinary)
