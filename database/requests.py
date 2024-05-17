import datetime
import logging

from sqlalchemy import select
from database.models import ExchangeRate

from database.settings import async_session


async def create_new_rate(
        exchange_rate: float,
        date: datetime.date,
) -> None:
    logging.info(f"New exchange rate: {exchange_rate}")
    async with async_session() as session:
        new_rate = ExchangeRate(datetime=date, exchange_rate=exchange_rate)
        session.add(new_rate)
        await session.commit()


async def get_rates():
    async with async_session() as session:
        result = await session.execute(select(ExchangeRate))
        return result.scalars().all()
