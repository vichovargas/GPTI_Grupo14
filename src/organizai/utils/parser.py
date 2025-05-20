import datetime

def parse_date(input_str: str) -> datetime.date:
    """Convierte 'MM-DD' o 'DD' en un objeto datetime.date, asumiendo el año actual."""
    today = datetime.date.today()
    current_year = today.year

    try:
        if "-" in input_str:
            month, day = map(int, input_str.split("-"))
        else:
            month = today.month
            day = int(input_str)
        return datetime.date(current_year, month, day)
    except Exception:
        raise ValueError("Fecha inválida. Usa 'MM-DD' o 'DD'.")


def parse_time(input_str: str) -> datetime.time:
    """Convierte entradas como '9', '13.5' o '9:30' en datetime.time."""
    try:
        if ":" in input_str:
            return datetime.time.fromisoformat(input_str)
        elif "." in input_str:
            hour, fraction = input_str.split(".")
            hour = int(hour)
            minutes = round(float("0." + fraction) * 60)
            return datetime.time(hour, minutes)
        else:
            return datetime.time(int(input_str), 0)
    except Exception:
        raise ValueError("Hora inválida. Usa '9', '9:30' o '13.5'")
