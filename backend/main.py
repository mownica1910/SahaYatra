from fastapi import FastAPI
from backend.database.connection import db

app = FastAPI(title="SahaYatra API")


@app.get("/")
def root():
    return {"message": "SahaYatra API is running"}


@app.get("/db-test")
def db_test():
    result = db.command("ping")
    return {"database": "connected", "result": result}