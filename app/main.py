from fastapi import FastAPI
from app.crud import router

app = FastAPI()

app.include_router(router)
