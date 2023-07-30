from fastapi import FastAPI

from src.routes.routes import route

app = FastAPI()

app.include_router(route, prefix="/api")
