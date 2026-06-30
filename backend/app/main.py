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