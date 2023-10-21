from aiogram import Router, F, Bot

from aiogram.types import Message, CallbackQuery

from aiogram.filters import Command

from keyboards import kb_start_reply, kb_start_inline, ikb_inline, SimpleCallBack

handlers_router = Router() # Создание сущности роутер.

@handlers_router.message(Command('start'))
async def com_start(message:Message):
    """
    Функция выполнения команды старт.
    """
    await message.answer('Привет друг!!!', reply_markup=kb_start_inline())
    # reply_markup=kb_start() - вызов кнопок из функции kb_start_inline()

@handlers_router.message(F.text == 'hello')
async def com_start(message:Message):
    await message.answer('Выбери кто ты?', reply_markup=ikb_inline(message.from_user.first_name))
    # reply_markup=kb_start() - вызов кнопок из функции kb_start_inline()

