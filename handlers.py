from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from database import requests
from utils.record_to_xlsx import record_to_excel

router = Router()


@router.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")


@router.message(Command(commands=["get_exchange_rate"]))
async def get_exchange_rate(message: Message):
    rates = await requests.get_rates()
    record_to_excel(rates)
    result = FSInputFile("result.xlsx")
    await message.answer_document(result)

