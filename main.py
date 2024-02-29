from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from aiogram import F


admin_ids = ['id private user']

F.from_user.id.in_(admin_ids)

BOT_TOKEN = 'your tokken'


# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    # работает только для приватных пользователей
    if message.from_user.id in admin_ids:
        await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
    # для всех остальных
    else:
        await message.answer(' are you?')



@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    if message.from_user.id in admin_ids:
        await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)