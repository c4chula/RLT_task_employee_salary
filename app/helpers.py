from datetime import datetime


def get_datetime_part(date: datetime, part: str) -> int | None:
    return {
        "year": date.year,
        "month": date.month,
        "day": date.day,
        "hour": date.hour,
    }.get([part], None)
