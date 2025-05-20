from pydantic import BaseModel
from typing import List, Literal
from datetime import time

class TimeRange(BaseModel):
    start_time: time
    end_time: time

class DailyAvailability(BaseModel):
    day: Literal['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    time_ranges: List[TimeRange]

class Availability(BaseModel):
    days: List[DailyAvailability]