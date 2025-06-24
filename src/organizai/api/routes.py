from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Literal
import json
import re
from datetime import datetime, date, time
from organizai.services.planner import generate_schedule
from organizai.models.task import Task
from organizai.models.availability import TimeRange, DailyAvailability, Availability

router = APIRouter()


class FrontendTask(BaseModel):
    id: str
    name: str
    duration: int
    dueDate: datetime
    priority: Literal["alta", "media", "baja"]
    createdAt: datetime


class FrontendAvailabilityBlock(BaseModel):
    id: str
    day: str
    startTime: str
    endTime: str


class ScheduleRequest(BaseModel):
    tasks: List[FrontendTask]
    availability: List[FrontendAvailabilityBlock]
    strategy: str


@router.post("/generate-schedule")
def create_schedule(request: ScheduleRequest):
    try:
        tasks = [
            Task(
                name=t.name,
                start_date=date.today(),
                end_date=t.dueDate.date(),
                estimated_hours=t.duration / 60,
                priority=t.priority,
            )
            for t in request.tasks
        ]

        daily = {}
        for block in request.availability:
            day = block.day.capitalize()
            if day not in daily:
                daily[day] = []
            daily[day].append(
                TimeRange(
                    start_time=datetime.strptime(
                        block.startTime, "%H:%M").time(),
                    end_time=datetime.strptime(block.endTime, "%H:%M").time(),
                )
            )

        availability = Availability(
            days=[
                DailyAvailability(day=day, time_ranges=ranges)
                for day, ranges in daily.items()
            ]
        )

        strategy = request.strategy.lower()

        raw_result = generate_schedule(tasks, availability, strategy)

        match = re.search(
            r"```(?:json)?\s*(\{.*\})\s*```", raw_result, re.DOTALL)
        cleaned_json = match.group(1) if match else raw_result

        parsed = json.loads(cleaned_json)

        return parsed

    except Exception as e:
        return {"error": str(e)}
