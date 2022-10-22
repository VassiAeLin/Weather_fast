from pydantic import BaseModel
from typing import List
import typing


class Weather(BaseModel):
    city = ''
    temp_c = []
    weather = []
    humidity = []
    wind = []
    pressure = []
    sunrise = []
    sunset = []

class Params(BaseModel):
    city = ''

class Format(Weather):
    dt = []


class Days(BaseModel):
    city = ''
    days = List[Weather]
    sunrise = ''
    sunset = ''

    class Config:
        arbitrary_types_allowed = True