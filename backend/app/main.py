from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.database import init_db
from backend.app.routers.users_routers import router as users_router
from backend.app.config import settings

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
    return {"message": "Hello World!"}
