import asyncio

import my_token

from aiogram import Dispatcher, Bot, F, Router

from aiogram.filters import Command # Фильтр сообщений

from aiogram.types import Message



token = my_token.my_token()

bot = Bot(token=token)

dp = Dispatcher()

general = Router()


@general.message(Command('start')) # Месеч хендлер ловец сообщений. Реакция на команду старт.

async def com_start(message: Message): # Функция, которая будет выполняться во время команды старт.
    """
    Выполнение команды старт.
    """
    print(message.from_user.id, message.from_user.full_name,sep='\t') # Вывод на печать id пользователя, который запускает команду.

    text = f'Здорова, {message.from_user.first_name}. Ты ебанат!'

    await bot.send_message(message.from_user.id, text=text) # Вывод текста в чат.



def on_start():
    """
    Функция выполняемая при старте бота.
    """
    print('Бот запущен!') 



def on_stop():
    """
    Функция запускается при останове бота.
    """
    print('Бот остановлен!')



async def start_bot():# Создаём функцию старта бота. Функция является асинхронной

    dp.include_router(general)

    dp.startup.register(on_start)# Запускается при старте бота. (Запускается функция on_start())

    dp.shutdown.register(on_stop)# Запускается при останове бота или аварийном останове. 

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot) # вызов из объекта процесса старта бота


if __name__ == '__main__':
    asyncio.run(start_bot()) # Запуск бота