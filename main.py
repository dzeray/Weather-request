import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import requests
from geopy import Nominatim
from tkcalendar import Calendar
from datetime import *
import json
from bs4 import BeautifulSoup

def get_weather(city, selected_date):
    api_key = ''
    base_url =''


    date_str = selected_date.strftime("%Y-%m-%d")
    params = {'q': city, 'appid': api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        for item in data['list']:
            if item['dt_txt'].split()[0] == date_str:
                print(date_str)
                print(city)
                weather_info = item['weather'][0]['description']
                temperature_kelvin = item['main']['temp']
                temperature_celsius = temperature_kelvin - 273.15
                result_label.config(text=f"Date: {date_str}\nCity: {city}\nWeather: {weather_info}\nTemperature: {temperature_celsius:.2f}°C")

                return

        result_label.config(text="No data available for the selected date.")

    except Exception as e:
        result_label.config(text=f"Error: {e}")

def on_submit():
    city = city_entry.get()
    selected_date_str =cal.get_date()
    selected_date = cal.strptime(selected_date_str, "%Y-%m-%d")

    if city:
        get_weather(city, selected_date)
    else:
        result_label.config(text="Please enter a city.")

window=tk.Tk()
window.title("WEATHER")


window.minsize(width=600,height=600)
image=Image.open("weather-app.png")
new_image=image.resize((500,200))
img=ImageTk.PhotoImage(new_image)
window.config(bg="blue")

top_label=tk.Label(image=img)
top_label.pack()
top_label.config(bg="blue")

select_label=tk.Label(text="Enter a city name",font=("Calibri", 10, "bold"))
select_label.config(bg="white", fg="black", width=20)
select_label.pack()

city_entry=tk.Entry(width=20)
city_entry.pack(padx=5, pady=5)
cities=city_entry.get()
city_entry.focus()
cal = Calendar(selectmode="day",date_pattern="Y-m-d")
cal.config(background="black", disabledbackground="black", bordercolor="black",
            headersbackground="blue", normalbackground="white", foreground='white',
            normalforeground='black', headersforeground='white')
cal.pack(padx=10,pady=10)


show_button=tk.Button(text="Show weather forecast",font=("Calibri", 10, "bold"),command=on_submit)
show_button.pack(padx=10, pady=10)

result_label=tk.Label(font=("Calibri", 10, "bold"))
result_label.pack(padx=3,pady=3)


window.mainloop()