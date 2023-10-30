from collections import OrderedDict
from typing import Dict


def get_ordered_types(field_name: str) -> Dict[str, Dict[str, str]]:
    return OrderedDict(
        {
            "year": {"$year": field_name},
            "month": {"$month": field_name},
            "day": {"$day": field_name},
            "hour": {"$hour": field_name},
        },
    )
