from asyncio import Task
from typing import Annotated

from fastapi import Depends
from pydantic import BaseModel, Field, ConfigDict




# from app.main import app


class FeedbackCreate(BaseModel):
    name: str = Field(max_length=20)
    phone: str = Field(max_length=10)
    description: str = Field(max_length=1000)
    city_id: int

    model_config = ConfigDict(extra='forbid') # Запрещает дополнительные поля








class CitySchema(BaseModel):
    id: int
    name: str
    phone: str
    price_multiplier: float

    class Config:
        orm_mode = True # Указываем, что этот класс используется для маппинга ORM объектов