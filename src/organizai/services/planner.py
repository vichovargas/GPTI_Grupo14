from organizai.models.task import Task
from organizai.models.availability import Availability
from organizai.services.gemini_client import call_gemini
from organizai.utils.prompt_loader import load_prompt_template

def generate_prompt(tasks: list[Task], availability: Availability) -> str:
    task_lines = [
        f'- Nombre: "{t.name}", Inicio: {t.start_date}, Fin: {t.end_date}, Estimado: {t.estimated_hours} horas, Prioridad: {t.priority}'
        for t in tasks
    ]
    
    availability_lines = []
    for day in availability.days:
        for tr in day.time_ranges:
            availability_lines.append(
                f"- {day.day}: {tr.start_time.strftime('%H:%M')} - {tr.end_time.strftime('%H:%M')}"
            )

    input_block = "**Tareas:**\n" + "\n".join(task_lines) + "\n\n**Disponibilidad:**\n" + "\n".join(availability_lines)

    template = load_prompt_template("scheduler_prompt")
    return template.replace("{input_data}", input_block)

def generate_schedule(tasks: list[Task], availability: Availability) -> str:
    prompt = generate_prompt(tasks, availability)
    return call_gemini(prompt)
