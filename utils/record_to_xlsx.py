import openpyxl
from openpyxl import Workbook


def record_to_excel(exchange_rates):
    wb = Workbook()
    ws = wb.active
    ws.append(["id", "datetime", "exchange_rate"])

    for rate in exchange_rates:
        ws.append([rate.id, rate.datetime, rate.exchange_rate])

    wb.save(f"result.xlsx")
