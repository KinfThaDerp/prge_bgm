from fastapi import FastAPI
from app.routes import static_content
app = FastAPI(title="Mapbook API")

app.include_router(static_content.router, prefix="/app")