from fastapi import FastAPI
import requests
import datetime
from schema import Weather, Params, Days, Format
import json
app = FastAPI()


@app.post('/weather')
async def get_weather(par: Params):
    try:
        API_key = "b646c06a4b45966cd21d98a9275e488c"
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={par.city}&appid={API_key}&units=metric&lang=ru")

        w_c = r.json()
        print(w_c)
        w = Weather()

        w.city = w_c["name"]
        w.temp_c = w_c["main"]["temp"]
        w.weather = w_c["weather"][0]["description"]
        w.humidity = w_c["main"]["humidity"]
        w.wind = w_c["wind"]["speed"]
        w.pressure = w_c["main"]["pressure"]
        w.sunrise = datetime.datetime.fromtimestamp(w_c["sys"]["sunrise"])
        w.sunset = datetime.datetime.fromtimestamp(w_c["sys"]["sunset"])


        return w.__dict__

    except Exception as ex:
        return ex.__str__()

@app.post('/weather/forecast_5')
async def get_weather(par: Params):
    try:
        API_key = "b646c06a4b45966cd21d98a9275e488c"
        r = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={par.city}&appid={API_key}&lang=ru")
        City = r.json()
        lat = City[0]["lat"]
        lon = City[0]["lon"]
        cnt = 40

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}&cnt={cnt}&units=metric&lang=ru")
        for5 = r.json()
        print(r.json())
        d = Days()
        f = Format()
        #
        # d.city = for5["city"]["name"]
        # d.sunrise = datetime.datetime.fromtimestamp(for5["city"]["sunrise"])
        # d.sunset = datetime.datetime.fromtimestamp(for5["city"]["sunset"])
        #
        # for i in range(0,cnt,8):
        #     d.days.append(for5["list"][i]["dt_txt"])
        #     d.temp_c.append(for5["list"][i]["main"]["temp"])
        #     d.weather.append(for5["list"][i]["weather"][0]["description"])
        #     d.humidity.append(for5["list"][i]["main"]["humidity"])
        #     d.wind.append(for5["list"][i]["wind"]["speed"])
        #     d.pressure.append(for5["list"][i]["main"]["pressure"])

        return d

    except Exception as ex:
        return ex.__str__()
