from fastapi import FastAPI
from app.routers import health, metrics, auth

app = FastAPI(
    title="Personal Metrics Dashboard",
    description="API for tracking personal metrics",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(metrics.router)
app.include_router(auth.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
