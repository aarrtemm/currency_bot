import datetime
from sqlalchemy import select
from models import ExchangeRate, async_session


async def create_new_rate(exchange_rate: float, date: datetime.date) -> None:
    async with async_session() as session:
        new_rate = ExchangeRate(rate=exchange_rate, date=date)
        session.add(new_rate)
        await session.commit()


async def get_rates():
    async with async_session() as session:
        rates = await session.scalars(select(ExchangeRate))
        return rates
