from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from organizai.api.routes import router

app = FastAPI(title="OrganizAI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")
