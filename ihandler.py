from aiogram import Router, Bot, F

from keyboards import SimpleCallBack

from aiogram.types import CallbackQuery


callback_router = Router()

@callback_router.callback_query(SimpleCallBack.filter(F.button == 'good'))
async def com_call(callback:CallbackQuery, call_back: SimpleCallBack):
    print(call_back)
    # await bot.send_message(f'Говорят, что ты {callback.data.name}')
    await callback.answer('Сам хуйло!!!',show_alert=True)