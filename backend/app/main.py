from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .routers.users_routers import router as users_router
from .config import settings
import uvicorn

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def hello_world():
    return {
        "message": "Hello World!",
        "docs": "api/docs"
    }

@app.get("/health")
def health():
    return {
        "status": "200_OK"
    }
