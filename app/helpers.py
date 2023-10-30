from collections import OrderedDict
from datetime import datetime
from typing import Dict

from dateutil.relativedelta import relativedelta


def get_ordered_types(field_name: str) -> Dict[str, Dict[str, str]]:
    return OrderedDict(
        {
            "year": {"$year": field_name},
            "month": {"$month": field_name},
            "day": {"$dayOfMonth": field_name},
            "hour": {"$hour": field_name},
        },
    )

def get_daterange_interval(type: str) -> relativedelta:
    return {
        "year": relativedelta(years=1),
        "month": relativedelta(months=1),
        "day": relativedelta(days=1),
        "hour": relativedelta(hours=1),
    }.get(type)

def get_list_of_daterange(by: str, left_date: datetime, right_date: datetime) -> list[str]:
    interval = get_daterange_interval(by)

    daterange = []
    while left_date <= right_date:
        daterange.append(left_date.isoformat())
        left_date += interval

    return daterange
