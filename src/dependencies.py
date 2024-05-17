from src.city_weather.db_managers.abstract_manager import AbstractDBManager
from src.city_weather.db_managers.city_manager import CityDBManager


def get_city_manager() -> AbstractDBManager:
    return CityDBManager()
