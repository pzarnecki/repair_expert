# app/main.py

from fastapi import FastAPI
from app.api.link4 import router as link4_router

app = FastAPI(title="Insurance API")

app.include_router(link4_router, prefix="/api/link4", tags=["Link4"])

@app.get("/")
def root():
    return {"Hey hey": "API dziala "}