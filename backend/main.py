from fastapi import FastAPI
from backend.database.connection import db
from backend.routes.user import router as users_router

app = FastAPI(title="SahaYatra API")

app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "SahaYatra API is running"}


@app.get("/db-test")
def db_test():
    result = db.command("ping")
    return {"database": "connected", "result": result}