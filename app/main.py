from fastapi import FastAPI
from app.routes import health, productivity, smart, personal, myday, news, memory, advice, focus

app = FastAPI(
    title="DreAPI",
    description="Private backend system for DreAI. Includes productivity, intelligence, personal automation, and system endpoints.",
    version="1.0.0",
    contact={
        "name": "Andre",
    }
)

app.include_router(health.router)
app.include_router(productivity.router)
app.include_router(smart.router)
app.include_router(myday.router)
app.include_router(news.router)
app.include_router(memory.router)
app.include_router(advice.router)
app.include_router(focus.router)


@app.get("/", tags=["System"], summary="Home")
def home():
    return {"message": "Welcome to DreAPI"}