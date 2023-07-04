from fastapi import FastAPI, Depends, HTTPException
from ecdsa.keys import SigningKey
from .database import SessionLocal, engine
from .database.database import Base
from sqlalchemy.orm import Session
from .crud.keys.create import create_key
from .crud.keys.read_key import read_key, read_public_key, read_private_key
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
    readed_key = read_key(db, device_id=device_id)
    if readed_key is not None:
        return {"error": "Device already registered"}
    priv_key = SigningKey.generate()  # NIST P-192
    pub_key = priv_key.verifying_key
    return create_key(
        db=db,
        key_model=DeviceKey(
            device_id=device_id, priv_key=priv_key.to_pem(), pub_key=pub_key.to_pem()
        ),
    )


@app.get("/query")
async def query_ecdsa_key(device_id: str, type: str, db: Session = Depends(get_db)):
    if type == "public":
        readed_key = read_public_key(db=db, device_id=device_id)
    if type == "private":
        readed_key = read_private_key(db=db, device_id=device_id)
    if type not in ["public", "private"]:
        return {"error": "Invalid key type requested"}
    if readed_key is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return {"data": readed_key}
