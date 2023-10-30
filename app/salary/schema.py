from datetime import datetime
from typing import List

from pydantic import BaseModel


class SalaryFilters(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: str


class SalaryAggregationResponse(BaseModel):
    dataset: List[int]
    labels: List[str]
