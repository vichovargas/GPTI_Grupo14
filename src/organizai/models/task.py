from pydantic import BaseModel, Field
from datetime import date
from typing import Literal


class Task(BaseModel):
    name: str
    start_date: date
    end_date: date
    estimated_hours: float = Field(..., gt=0)
    priority: Literal["alta", "media", "baja"]
