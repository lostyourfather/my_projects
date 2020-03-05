import pyowm
city = input("What is city?: ")
owm = pyowm.OWM('55dc960512c3a0f6ce8417a61cabd7b8', language="ru")
try:
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    windSpeed = w.get_wind()
    humidity = w.get_humidity()
    status = w.get_detailed_status()
    print("Temperature in " + city + " " + str(w.get_temperature("celsius")["temp"]) + " degree " + "status: " + str(status) + " speed of wind: " + str(windSpeed["speed"]) + " m/s " + "humidity: " + str(humidity))

except:
    print(1)
