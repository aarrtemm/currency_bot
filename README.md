# This project is a Telegram bot built using aiogram, alembic, and SQLalchemy. It provides a simple framework for creating and managing a Telegram bot with database support.

## 1. Clone the repository:
  ``` bash
  git clone https://github.com/your_username/currency_bot.git

  cd currency_bot
  ```

## 2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## 3. Create a new bot using BotFather.
  - Copy the token provided by BotFather.
  - Add the database url to ```.env``` file.
  - Add the following line to the ```.env``` file, replacing YOUR_BOT_TOKEN and YOUR_URL with your bot token:
    ```bash
    TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN

    SQLALCHEMY_URL=YOUR_URL
    
    ```
## 4. Set up your database:
  - Update the database configurations in config.py according to your database setup.
  - Run alembic migrations to create the necessary tables:
    ```bash
    alembic upgrade head
    ```

## Usage
 ### Run the bot:
  ```bash
  python run.py
  ```
    
