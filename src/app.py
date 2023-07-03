from fastapi import FastAPI

app = FastAPI()


@app.get("/generate/")
async def generate_ecdsa_pair(device_id: str):
    passs
