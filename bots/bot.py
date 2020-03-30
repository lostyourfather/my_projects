import telebot
import pyowm

bot = telebot.TeleBot("1087470565:AAHKtxzBruFyG2uQDb5cv97uS-5lHvJohSs")
owm = pyowm.OWM('55dc960512c3a0f6ce8417a61cabd7b8', language="en")


@bot.message_handler(content_types=["text"])
def send_welcome(message):
    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        windSpeed = w.get_wind()
        humidity = w.get_humidity()
        status = w.get_detailed_status()
        answer = "In city " + message.text + " " + str(
            w.get_temperature("celsius")["temp"]) + " degree " + "status: " + str(status) + " speed of wind: " + str(
            windSpeed["speed"]) + " m/s " + "humidity: " + str(humidity)
        bot.send_message(message.chat.id, answer)
    except:
        bot.send_message(message.chat.id, "I don't know this city")


bot.polling(none_stop=True)
