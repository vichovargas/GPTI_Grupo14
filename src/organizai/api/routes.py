from fastapi import APIRouter
from organizai.models.task import Task
from organizai.models.availability import Availability
from organizai.services.planner import generate_schedule
from typing import List
from pydantic import BaseModel

router = APIRouter()

class ScheduleRequest(BaseModel):
    tasks: List[Task]
    availability: Availability

@router.post("/schedule/")
def create_schedule(request: ScheduleRequest):
    try:
        result = generate_schedule(request.tasks, request.availability)
        return {"schedule": result}
    except Exception as e:
        return {"error": str(e)}
