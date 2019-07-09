import tkinter as tk
import os
from tkinter import font
import requests

Height, Width = 500, 600
font_style = ('Courier New', 12)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# api-key(weather_key): 9d3f2e1e760fc73709c43804c7ere46a etc...
# read>>how_to_get_api_key.txt

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        ico = weather['weather'][0]['icon']
        icon = weather_icons[ico]

        final_str = 'City: %s \nConditions: %s \nTemperature(°F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information!'

    return final_str, icon

def get_weather(city):
    weather_key = '9d3f2e1e760fc73709c43804c7ere46a'	# your api-key (this is fake api_key)
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather = response.json()

        label['text'], icon_label['image'] = format_response(weather)
    except Exception as exc:
        label['text'] = "There was a problem retrieving \nthat information! Try again..."
        icon_label.config(image='')


root = tk.Tk()
root.title("Weather App")
root.resizable(0, 0)

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

# background image
background_image = tk.PhotoImage(file='images/dearhd.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# top frame
frame = tk.Frame(root, bg='#53bcf5', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=font_style)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=font_style, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# lower frame
lower_frame = tk.Frame(root, bg='#53bcf5', bd=8)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# importing icons
weather_icons = {}
for filename in os.listdir('./img'):
    weather_icons[filename[:3]] = tk.PhotoImage(file='./img/'+filename)

label = tk.Label(lower_frame, bg = '#fff', font=font_style, anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

icon_label = tk.Label(lower_frame, bg= '#fff', anchor='w', justify='left', bd=4)
icon_label.place(relx=0.8, relwidth=0.2, relheight=0.25)

root.mainloop()
