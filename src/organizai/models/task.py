from pydantic import BaseModel, Field
from datetime import date

class Task(BaseModel):
    name: str
    start_date: date
    end_date: date
    estimated_hours: float = Field(..., gt=0)
    priority: int = Field(..., ge=1, le=10)
