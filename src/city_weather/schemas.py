from pydantic import BaseModel, ConfigDict
from pydantic.v1 import validator


class CityBase(BaseModel):
    name: str
    country: str
    additional_info: str | None = None


class CityCreate(CityBase):

    @validator("name")
    def validate_city_name(cls, name: str):
        if len(name) > 255:
            raise ValueError("City's name is too long")
        return name

    @validator("country")
    def validate_city_name(cls, country: str):
        if len(country) > 255:
            raise ValueError("Country's name is too long")
        return country


class City(CityBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

