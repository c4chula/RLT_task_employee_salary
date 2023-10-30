
import logging

from aiogram import Router
from aiogram.types import Message

from app.salary.schema import SalaryAggregationResponse, SalaryFilters
from app.salary.service import SalaryService

salary_router = Router(name=__name__)


@salary_router.message()
async def get_agregation_data(msg: Message) -> None:

    salary_filters: SalaryFilters
    try:
        salary_filters = SalaryFilters.model_validate_json(msg.text)
    except ValueError:
        logging.exception("json is not valid")
        await msg.answer(f"{msg.text}\n\nIs not valid!")

    result: SalaryAggregationResponse = await SalaryService().get_salary_aggregation(salary_filters)
    await msg.answer(f"{result}")
