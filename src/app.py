from fastapi import FastAPI, Depends
from ecdsa.keys import SigningKey
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()


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
