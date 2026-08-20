from fastapi import FastAPI
from server.routes import vision

app = FastAPI(
    title="Smart Classroom Vision API",
    description="Backend API for Smart Classroom system: processes video frames and detects students.",
)


app.include_router(vision.router)

@app.get("/")
def root():
    return {"message": "Welcome to Smart Classroom Vision API"}