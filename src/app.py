from fastapi import FastAPI, Depends
from ecdsa.keys import SigningKey
from .database import SessionLocal, engine
from .database.database import Base
from sqlalchemy.orm import Session
from .crud.keys.create import create_key
from .entities.key import DeviceKey

app = FastAPI()

Base.metadata.create_all(bind=engine)


# Dependency for use independent database across request, also can replace the database whith other implementation
# across the projects
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/generate/")
async def generate_ecdsa_pair(device_id: str, db: Session = Depends(get_db)):
    priv_key = SigningKey.generate()  # NIST P-192
    pub_key = priv_key.verifying_key
    return create_key(
        db=db,
        key_model=DeviceKey(
            device_id=device_id, priv_key=priv_key.to_pem(), pub_key=pub_key.to_pem()
        ),
    )
