from datetime import datetime
from enum import StrEnum
from typing import List

from pydantic import BaseModel


class SalaryFiltersGroupTypeEnum(StrEnum):
    year = "year"
    month = "month"
    day = "day"
    hour = "hour"


class SalaryFilters(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: str

    # @validator("group_type", pre=True)
    # def group_type_is_valid(cls, group_type: str) -> SalaryFiltersGroupTypeEnum:
    #     try:
    #         group_type_enum = SalaryFiltersGroupTypeEnum(group_type)
    #     except ValueError:
    #         logging.exception(f"group_type is not valid: {group_type}")
    #     return group_type_enum


class SalaryAggregationResponse(BaseModel):
    dataset: List[int]
    labels: List[str]
