from aiogram import Router

salary_router = Router(name=__name__)

@salary_router.message()
async def get_agregation_data() -> None:
    ...
