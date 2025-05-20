from pydantic import BaseModel
from typing import List, Literal
from datetime import time

class TimeRange(BaseModel):
    start_time: time
    end_time: time

class DailyAvailability(BaseModel):
    day: Literal['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    time_ranges: List[TimeRange]

class Availability(BaseModel):
    days: List[DailyAvailability]