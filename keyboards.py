# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType # Работа с клавиатурой.


# btn_start = KeyboardButton(text='Телефон', request_contact=True) # Создание кнопки старт.
# # request_contact=True будет запрашивать наш контакт (т.е. мой номер телефона!!!)
# btn_finish = KeyboardButton(text='Геометка',request_location=True) # Создание кнопки стоп.
# # request_location=True Отправление геометки
# btn_golos = KeyboardButton(text='Голосование', request_poll=KeyboardButtonPollType(type='Викторина'))
# # Создание кнопки голосование
# kb_set = [[btn_start,btn_finish,btn_golos]] # Создание списков списков кнопок.
# keyboard = ReplyKeyboardMarkup(keyboard=kb_set,resize_keyboard=True, one_time_keyboard=True,
#                                 input_field_placeholder='А ну напиши чего-нибудь!') # Создание клавиатуры.
# # resize_keyboard=True - для уменьшения кнопок
# # one_time_keyboard=True - создание одноразовой клавиатуры. Нажали она исчезла.
# #input_field_placeholder='А ну напиши чего-нибудь!' - Запись в строку набора сообщения всплывающего текста

# Работа с клавиатурой

from aiogram.utils.keyboard import ReplyKeyboardBuilder,\
                                    InlineKeyboardBuilder 

from aiogram.types import KeyboardButton

from aiogram.filters.callback_data import CallbackData


class SimpleCallBack(CallbackData, prefix = 'scb'):
    button: str 
    text: str = ''
    name: str = ''


def kb_start_reply():
    """
    Функция вызова кнопок. Создание шаблонной клавиатуры. 
    """
    keyboard = ReplyKeyboardBuilder() # Создание сущности клавиатуры Builder (строитель)
    #keyboard.button(text='Сова') # Создание одной кнопки Сова кнопки

    for i in range(1,17):# Передача цифровой клавиатуры от 1 до 16. Ново введение aiogram 3,0
        keyboard.button(text=str(i)) # Создание кнопки
    
    keyboard.adjust(4,2,3) # Создание кнопок в 4 ряда. Каждая цифра означает, сколько кнопок в строке.

    return keyboard.as_markup(resize_keyboard = True, one_time_keyboard=True) # Возвращение кнопки
    # resize_keyboard=True - уменьшение размера кнопок.
    # one_time_keyboard=True - создание одноразовой клавиатуры. Нажали кнопку она исчезла.


def kb_start_inline():
    """
    Функция вызова кнопок. Создание шаблонной клавиатуры. 
    """
    keyboard = InlineKeyboardBuilder() # Создание сущности клавиатуры Inline
    #keyboard.button(text='Сова') # Создание одной кнопки Сова кнопки

    for i in range(1,17):# Передача цифровой клавиатуры от 1 до 16. Ново введение aiogram 3,0
        keyboard.button(text=str(i),callback_data=SimpleCallBack(button='press')) # Создание кнопки
        # text=str(i) Подпись на кнопке
        # callback_data='1'- функционал, который выполняет кнопка.
    keyboard.adjust(4,2,3) # Создание кнопок в 4 ряда. Каждая цифра означает, сколько кнопок в строке.

    return keyboard.as_markup(resize_keyboard = True, one_time_keyboard=True) # Возвращение кнопки
    # resize_keyboard=True - уменьшение размера кнопок.
    # one_time_keyboard=True - создание одноразовой клавиатуры. Нажали кнопку она исчезла.

def ikb_inline(name: str):
    ikeboard = InlineKeyboardBuilder
    ikeboard.button(text = 'Молодец!!!', callback_data=SimpleCallBack(button='good', name=name))
    ikeboard.button(text = 'Чёрт', callback_data=SimpleCallBack(button='bad', name=name), self=True)
    return ikeboard.as_markup()