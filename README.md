# Weather Bot

A robust and user-friendly Weather bot developed using [Aiogram 3](https://docs.aiogram.dev/en/latest/) for Telegram and powered by [FastAPI](https://fastapi.tiangolo.com/) as the server, also uses [OpenWeather](https://openweathermap.org/) to get weather information. This bot fetches real-time weather information based on city names, providing users with quick and accurate weather updates.

## Features

- **City-Based Weather Information**: Simply type the name of a city to receive instant weather data, including temperature and conditions.
- **Real-Time Updates**: Access the latest weather information from reliable APIs for an accurate forecast.
- **User-Friendly Interface**: Designed for ease of use, making it accessible for all Telegram users.
- **Modular Architecture**: The code is structured in a modular way, ensuring easy maintenance and updates.

## Instalation

1. **First, select the location where you want to install the bot:**
```bash
cd <your-repository-folder>
```
2. **Next, clone the repository:**
```bash
git clone https://github.com/PixisProd/telegram-todo-bot.git #######################
```
3. **After which you can optionally create a virtual environment, this is not necessary, but I would recommend:**
```bash
python -m venv .env
```
4. **Next you need to install the dependencies:**
```bash
pip install -r requirements.txt
```
5. **In order for Telegram to see our fastapi server on the local machine, you need to use [ngrok](https://ngrok.com/download).**

## Preparation

1. Create a telegram bot using [BotFather](https://telegram.me/BotFather) and get your bot token, or if you already have a bot, then take an existing one.

2. Then find the `config.py` file in the project and paste your bot's token into the `TELEGRAM_BOT_TOKEN` field.

3. **Open `ngrok.exe` and enter the following command:**
```bash
ngrok http <your-port>
```
4. After you see that in ngrok `Session status` is `online` and lights up green, then the tunnel is ready to work through the port you selected. **Be sure to remember the port you specified.**

5. In the left column you need to find the `Forwarding` field and copy the url that ends with `.ngrok-free.app`.

6. Open the `config.py` file and paste the url we got in the paragraph above into the `NGROK_TUNNEL_URL` field.

7. Register on [OpenWeather](https://home.openweathermap.org/api_keys) and get your api key.

8. Open the `config.py` file and paste your api key that you got in the step above into the `WEATHER_API_KEY` field.

## Bot startup

After all these preparations, we can finally start working with our bot.

1. **Activate your virtual environment:**
```bash
<directory>/.env/Scripts/activate
```
Here `.env` is the name of your virtual environment, if you changed it when creating it, then replace `.env` with the name of your environment

2. **Start FastAPI server:**
```bash
uvicorn main:app --host 0.0.0.0 --port <your-port>
```
Here `your-port` is the port you specified when creating the tunnel to ngrok.

After all this, your bot is ready to work.

## Conclusion

Feel free to contribute to the project by reporting issues, suggesting features, or submitting pull requests. Your feedback and contributions are always welcome!

_Good weather to you! 🎉_