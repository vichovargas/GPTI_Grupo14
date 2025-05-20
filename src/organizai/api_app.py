from fastapi import FastAPI
from organizai.api.routes import router

app = FastAPI(title="OrganizAI API")

app.include_router(router, prefix="/api")
