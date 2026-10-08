from fastapi import FastAPI

app = FastAPI(title="License Tracker API", version="0.1.0")

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/about")
def about():
    return {"project": app.title, "version": app.version, "status": "ok"}

