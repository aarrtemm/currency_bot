import logging
import os
import requests
import lxml
from bs4 import BeautifulSoup


BASE_URL = "https://www.google.com/finance"
F_CURRENCY = "USD"
S_CURRENCY = "UAH"
TARGET_URL = f"{BASE_URL}/quote/{F_CURRENCY}-{S_CURRENCY}"


def get_exchange_rate() -> float:
    try:
        response = requests.get(TARGET_URL)
        with open("page.html", "w") as file:
            file.write(response.text)
        with open("page.html") as file:
            src = file.read()
        soup = BeautifulSoup(src, "lxml")
        price = soup.find("div", {"data-last-price": True})["data-last-price"]
        delete_file()
        return float(price)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return 0.0


def delete_file():
    try:
        os.remove("page.html")
    except Exception as e:
        logging.error(f"Failed to delete file: {e}")
