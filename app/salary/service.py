from typing import Any

from app.database import MotorAsyncSessionfactory
from app.salary.repo import SalaryRepo
from app.salary.schema import SalaryFilters


class SalaryService(MotorAsyncSessionfactory):

    def __init__(self) -> None:
        ...

    async def get_salary_aggregation(self, schema: SalaryFilters) -> Any:
        db_session = await super().get_client_session()
        return await SalaryRepo(db_session).get_salary_aggregation()

