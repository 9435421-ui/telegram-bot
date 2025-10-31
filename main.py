from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio

BOT_TOKEN = "8300288333:AAFg14rPHAFxJ1LQvwrdIJ4HdQFg2qUc4ec"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Бот работает! Напиши что-нибудь.")

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
