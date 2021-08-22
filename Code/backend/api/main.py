from fastapi import FastAPI
from mongoengine import connect
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from api.routes.places import router as places_route
from api.routes.feedback import router as feedback_route


def app_factory() -> FastAPI:
    """Factory for our application"""
    connect(host=settings.DB_HOST)
    app = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        version=settings.VERSION
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = app_factory()
app.include_router(places_route)
app.include_router(feedback_route)
