

from app.database import MotorAsyncSessionfactory
from app.helpers import get_list_of_daterange
from app.salary.repo import SalaryRepo
from app.salary.schema import SalaryAggregationResponse, SalaryFilters


class SalaryService(MotorAsyncSessionfactory):
    def __init__(self) -> None:
        ...

    async def get_salary_aggregation(
        self,
        schema: SalaryFilters,
    ) -> SalaryAggregationResponse:
        db_session = await super().get_client_session()
        docs = await SalaryRepo(db_session).get_salary_aggregation(
            dt_from=schema.dt_from,
            dt_upto=schema.dt_upto,
            group_type=schema.group_type,
        )

        labels = get_list_of_daterange(schema.group_type, schema.dt_from, schema.dt_upto)

        dataset = []
        i = j = 0
        while j < len(labels):
            if (i < len(docs) and docs[i].get("_id").isoformat() != labels[j]) or i >= len(docs):
                dataset.append(0)
            elif docs[i].get("_id").isoformat() == labels[j]:
                dataset.append(docs[i].get("sum"))
                i += 1
            j += 1

        return SalaryAggregationResponse(
            dataset=dataset,
            labels=labels,
        )
