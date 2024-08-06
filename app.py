import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk


def get_weather():
    city = city_input.get()
    api_key = '30d4741c779ba94c470ca1f63045390a'
    try:
        weather_api_request = (
            requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"))
        if weather_api_request.json()['cod'] == '404':
            messagebox.showerror("Invalid City credentials")
        else:
            weather_info = (f"The weather in {city} is {weather_api_request.json()['main']['temp']}F, described by: "
                            f"{weather_api_request.json()['weather'][0]['description']}")
            weather_label.config(text=weather_info)
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Weather App")

#Image
image_path = "image.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)

#Textfield
tk.Label(root, text="Enter a City").pack(pady=10)
city_input = tk.Entry(root)
city_input.pack(pady=5)

#Button
tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)
weather_label = tk.Label(root, text="")
weather_label.pack(pady=20)

root.mainloop()
