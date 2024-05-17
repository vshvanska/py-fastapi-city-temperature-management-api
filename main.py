from typing import List
from fastapi import FastAPI, Depends
from src.city_weather.db_managers.city_manager import CityDBManager
from src.city_weather.schemas import CityCreate, City
from src.dependencies import get_city_manager

app = FastAPI()


@app.get("/cities/", response_model=List[City])
async def retrieve_cities(manager: CityDBManager = Depends(get_city_manager)):
    return await manager.get_list_of_items()


@app.post("/cities/")
async def retrieve_cities(city: CityCreate, manager: CityDBManager = Depends(get_city_manager)):
    return await manager.create_new_item(data=city)


@app.get("/cities/{city_id}/", response_model=City)
async def retrieve_cities(city_id: int, manager: CityDBManager = Depends(get_city_manager)):
    return await manager.get_item_by_id(city_id)


@app.put("/cities/", response_model=City)
async def retrieve_cities(city: City, manager: CityDBManager = Depends(get_city_manager)):
    return await manager.update_item(data=city)


@app.delete("/cities/{city_id}/")
async def retrieve_cities(city_id: int, manager: CityDBManager = Depends(get_city_manager)):
    return await manager.delete_item(city_id)


