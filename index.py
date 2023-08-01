from fastapi import FastAPI

from db import get_engine


app = FastAPI()

try:
    session, Base = get_engine()
    if session is not None and Base is not None:
        from src.routes.routes import route
        app.include_router(route, prefix="/api")
except Exception:
    pass
