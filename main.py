from math import trunc
from sys import prefix
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from config.database import db
from routers.userRoute import router as user_router
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Only allow requests from your React app
    allow_credentials=True,
    allow_methods=["POST","GET","PUT","PATCH","DELETE"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(user_router, prefix="/api/auth")


@app.get("/")
async def home():
    return "<h1>Server Work Perfect....</h1>"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=6000, reload=True)
