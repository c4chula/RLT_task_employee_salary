import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils import markdown

from app.config import cfg
from app.salary.routers import salary_router

dp = Dispatcher()

main_router = Router(name=__name__)
main_router.include_router(salary_router)

dp.include_router(main_router)

@main_router.message(CommandStart())
async def command_start_handler(msg: Message) -> None:
   await msg.answer(f"Hello, {markdown.hbold(msg.from_user.full_name)}!")


async def main() -> None:
    bot = Bot(cfg.BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
