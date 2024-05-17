from fastapi import FastAPI
from src.city_weather.routers import city_router

app = FastAPI()

app.include_router(city_router)
