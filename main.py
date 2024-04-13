from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.get_cv_db import cv_router

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cv_router.router)