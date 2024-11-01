from aiogram import types, Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from config import TELEGRAM_BOT_TOKEN
from keyboards import get_start_keyboard
from weatherAPI import get_weather_by_name
from emoj_related import *

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

class GetWeather(StatesGroup):
    get_input = State()

# Start command handler
@dp.message(CommandStart())
async def start(message: types.Message):
    answer = (
        f"<b>👋 Hello!</b>\n"
        f"I'm your assistant for getting weather information. 🌤️\n"
        f"Type <b>/help</b> for more information.\n"
    )

    photo = types.FSInputFile(path='img\\weather-bot-greeting-image.jpg')
    await message.answer_photo(photo=photo, caption=answer, reply_markup=get_start_keyboard(), parse_mode='HTML')

# Help command handler
@dp.message(Command('help'))
async def help(message: types.Message):
    answer = (
        f"<b>ℹ️ Help - Weather Bot</b>\n\n"
        f"<b>🌤️ I can help you get the weather information!</b>\n\n"
        f"Here's what I can do:\n"
        f"- <b>Get weather info by city name</b> 🌆\n"
        f"<b>🌟 Let's get started!</b> Press <i>'☁ Get weather'</i> to begin."
    )
    await message.answer(text=answer, parse_mode='HTML', reply_markup=get_start_keyboard())

# Get weather information
@dp.message(F.text == "☁ Get weather")
async def get_weather(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text="🌍✨ <b>Please enter the name of the city</b> you'd like to know the weather for! 🌦️", 
                         parse_mode='HTML')
    await state.set_state(GetWeather.get_input)

@dp.message(GetWeather.get_input)
async def get_weather_get_input(message: types.Message, state: FSMContext):
    data = get_weather_by_name(name=message.text)
    if data["cod"] == 200:
        answer = (
            f'{get_country_flag(data)} <b><i>{data["name"]}</i></b>\n'
            f'🌡️ <b>Temperature:</b> {int(data["main"]["temp"])}°C\n'
            f'{get_emohi_for_feels_like(data)} <b>Feels like:</b> {int(data["main"]["feels_like"])}°C\n'
            f'💧 <b>Humidity:</b> {data["main"]["humidity"]}%\n'
            f'{get_emoji_for_description(data)} <b>Descripton:</b> {data["weather"][0]["description"].capitalize()}'
        )
        await state.clear()
    else:
        answer = f'Wrong city name'

    await message.answer(text=answer, parse_mode='HTML')

# Echo method
@dp.message(F.text)
async def echo(message: types.Message):
    await message.answer(text=message.text)