from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import upload, summarize, qa, critique
from app.db.mongo import init_db
import uvicorn

app = FastAPI(title="AstraPaper", version="1.0.0")

# ✅ Add CORS middleware
origins = [
    "http://localhost:5173",   # React dev server
    "http://127.0.0.1:5173",   # sometimes React uses this
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # allowed frontend origins
    allow_credentials=True,
    allow_methods=["*"],          # allow all HTTP methods
    allow_headers=["*"],          # allow all headers
)

# Routers
app.include_router(upload.router, prefix="/api")
app.include_router(summarize.router, prefix="/api")
app.include_router(qa.router, prefix="/api")
app.include_router(critique.router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    await init_db()
    print("Database initialized")
    print("Application startup complete")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
