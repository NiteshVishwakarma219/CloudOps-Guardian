from fastapi import FastAPI

from app.api.v1 import (
    ec2,
    dashboard,
    cost,
    security
)

app = FastAPI(
    title="CloudOps Guardian",
    version="1.0.0"
)

app.include_router(ec2.router)
app.include_router(dashboard.router)
app.include_router(cost.router)
app.include_router(security.router)


@app.get("/")
def home():
    return {
        "application": "CloudOps Guardian",
        "status": "Running",
        "version": "1.0.0"
    }

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:3000",
        "http://localhost:3000",
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)