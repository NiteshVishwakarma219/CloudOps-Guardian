from fastapi import FastAPI
from app.routers import ec2

app = FastAPI(
    title="CloudOps Guardian API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "CloudOps Guardian API is running"
    }

app.include_router(ec2.router)