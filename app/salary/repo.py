from typing import TYPE_CHECKING, Any, Dict, Sequence

from motor.motor_asyncio import AsyncIOMotorClientSession

from app.config import cfg
from app.salary.schema import SalaryFiltersGroupTypeEnum

if TYPE_CHECKING:
    from datetime import datetime


class SalaryRepo:
    def __init__(
        self, db_session: AsyncIOMotorClientSession, db_name: str | None = None,
    ) -> None:
        self.db_session = db_session
        self.db_name = cfg.DB_NAME

    async def get_salary_aggregation(self, **filters: Dict[str, Any]) -> Sequence[Dict[str, Any]]:
        dt_from: datetime = filters.get("dt_from", None)
        dt_upto: datetime = filters.get("dt_upto", None)
        group_type: datetime = filters.get("group_type", None)

        group_date_parts: Dict[str, int] = {}

        for part in SalaryFiltersGroupTypeEnum:
            group_date_parts[part] = f"${part}"
            if part == group_type:
                break

        cursor = self.db_session.client[cfg.DB_NAME][cfg.DB_COLLECTION_NAME].aggregate(
            [
                {
                    "$match": {
                        "dt": {"$gte": dt_from, "$lte": dt_upto},
                    },
                    "$group": {
                        "_id": {
                            "$dateFromParts": group_date_parts,
                        },
                        "count": {"$sum": "$value"},
                    },
                },
                {"$sort": {"_id": 1}},
            ],
        )

        return await cursor.to_list(None)
