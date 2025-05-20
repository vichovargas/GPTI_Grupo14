from organizai.models.task import Task
from organizai.models.availability import Availability, DailyAvailability, TimeRange
from organizai.services.planner import generate_schedule
from organizai.utils.parser import parse_date, parse_time


# --------- Entrada de datos ---------

def input_task() -> Task:
    print("\n--- Nueva tarea ---")
    name = input("Nombre: ")
    start = parse_date(input("Fecha de inicio (MM-DD o DD): "))
    end = parse_date(input("Fecha de fin (MM-DD o DD): "))
    hours = float(input("Horas estimadas de estudio: "))
    priority = int(input("Prioridad (1-10): "))
    return Task(name=name, start_date=start, end_date=end, estimated_hours=hours, priority=priority)


def input_availability() -> Availability:
    print("\n--- Disponibilidad semanal ---")
    print("Escribe los días (Lunes–Domingo). Deja vacío para terminar.\n")
    availability_by_day = []

    while True:
        day = input("Día: ").strip()
        if not day:
            break

        time_ranges = []
        while True:
            start_input = input(f"  Inicio ({day}) [ej. 9, 13.5, 9:30] (vacío para terminar): ").strip()
            if not start_input:
                break
            end_input = input(f"  Fin   ({day}) [ej. 11, 15.5, 11:30]: ").strip()

            try:
                start_time = parse_time(start_input)
                end_time = parse_time(end_input)
                time_ranges.append(TimeRange(start_time=start_time, end_time=end_time))
            except ValueError as e:
                print(f"  {e}")

        if time_ranges:
            availability_by_day.append(DailyAvailability(day=day, time_ranges=time_ranges))

    return Availability(days=availability_by_day)


# --------- Interfaz principal ---------

def show_menu():
    print("\n=== OrganizAI ===")
    print("1. Ingresar tarea")
    print("2. Ingresar disponibilidad")
    print("3. Generar cronograma")
    print("4. Salir")


def main():
    tasks = []
    availability = None

    while True:
        show_menu()
        choice = input("Opción: ").strip()

        if choice == "1":
            try:
                task = input_task()
                tasks.append(task)
                print(f'tareas -> {tasks}')
                print("✓ Tarea añadida.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                availability = input_availability()
                print("✓ Disponibilidad registrada.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            print(f'tareas -> {tasks}')
            print(f'disponibilidad -> {availability}')
            if not tasks or not availability:
                print("⚠ Debes ingresar al menos una tarea y disponibilidad.")
                continue
            print("\nGenerando cronograma con IA...")
            result = generate_schedule(tasks, availability)
            print("\n--- CRONOGRAMA GENERADO ---\n")
            print(result)

        elif choice == "4":
            print("Hasta luego.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
