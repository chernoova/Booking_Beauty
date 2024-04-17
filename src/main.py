import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy

from src.config import EnvSettings
from routers import registration, menu, appointment, saloon
from src.middlewaries.database_middleware import DatabaseMiddleware

dp = Dispatcher(storage=MemoryStorage(), FSMStrategy=FSMStrategy.USER_IN_CHAT)
dp.update.middleware(DatabaseMiddleware())


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    bot = Bot('6357080266:AAEpilOn7y2QT5awRMF7Qa6cwlMxTpkcryY')

    dp.include_router(registration.router)
    dp.include_router(menu.router)
    dp.include_router(appointment.router)
    dp.include_router(saloon.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())