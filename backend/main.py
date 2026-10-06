from fastapi import FastAPI

app = FastAPI(title="SahaYatra API")


@app.get("/")
def root():
    return {"message": "SahaYatra API is running"}