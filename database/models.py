from sqlalchemy import Column, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True)
    datetime = Column(String)
    exchange_rate = Column(Float)
