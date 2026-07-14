"""
Weather App
Oasis Infobyte - Python Internship Project
Author: Abeer Fatima
"""

import tkinter as tk
from tkinter import messagebox
import urllib.request
import json

# ---------- Colors (pastel theme) ----------
BG_COLOR = "#fdf6ec"
CARD_COLOR = "#ffffff"
ACCENT_COLOR = "#a7c7e7"
ACCENT_DARK = "#87b0d6"
TEXT_COLOR = "#4a4a4a"
SUBTEXT_COLOR = "#9a9a9a"
ENTRY_BG = "#f3f0ea"
SUNNY_COLOR = "#ffd97d"
RAINY_COLOR = "#9ec9e2"

FONT_TITLE = ("Segoe UI", 22, "bold")
FONT_LABEL = ("Segoe UI", 13)
FONT_ENTRY = ("Segoe UI", 13)
FONT_TEMP = ("Segoe UI", 34, "bold")
FONT_DESC = ("Segoe UI", 14)
FONT_DETAIL = ("Segoe UI", 11)

WEATHER_CODES = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "🌤️"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Fog", "🌫️"),
    48: ("Fog", "🌫️"),
    51: ("Light drizzle", "🌦️"),
    53: ("Drizzle", "🌦️"),
    55: ("Heavy drizzle", "🌧️"),
    61: ("Light rain", "🌧️"),
    63: ("Rain", "🌧️"),
    65: ("Heavy rain", "🌧️"),
    71: ("Light snow", "🌨️"),
    73: ("Snow", "🌨️"),
    75: ("Heavy snow", "❄️"),
    80: ("Rain showers", "🌦️"),
    95: ("Thunderstorm", "⛈️"),
}


def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Missing Input", "Please enter a city name.")
        return

    try:
        # Step 1: Geocoding - get lat/lon for the city
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={urllib.parse.quote(city)}&count=1"
        with urllib.request.urlopen(geo_url, timeout=10) as resp:
            geo_data = json.loads(resp.read().decode())

        if "results" not in geo_data or not geo_data["results"]:
            messagebox.showerror("Not Found", f"Could not find city: {city}")
            return

        result = geo_data["results"][0]
        lat = result["latitude"]
        lon = result["longitude"]
        display_name = f"{result['name']}, {result.get('country', '')}"

        # Step 2: Fetch current weather
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
            f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
        )
        with urllib.request.urlopen(weather_url, timeout=10) as resp:
            weather_data = json.loads(resp.read().decode())

        current = weather_data["current"]
        temp = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind = current["wind_speed_10m"]
        code = current["weather_code"]

        description, emoji = WEATHER_CODES.get(code, ("Unknown", "🌡️"))

        city_label.config(text=display_name)
        emoji_label.config(text=emoji)
        temp_label.config(text=f"{temp:.1f}°C")
        desc_label.config(text=description)
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind: {wind} km/h")

    except urllib.error.URLError:
        messagebox.showerror("Connection Error", "Could not connect to weather service. Check your internet.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")


def clear_fields():
    city_entry.delete(0, tk.END)
    city_label.config(text="")
    emoji_label.config(text="🌡️")
    temp_label.config(text="--°C")
    desc_label.config(text="Enter a city to check weather")
    humidity_label.config(text="")
    wind_label.config(text="")


import urllib.parse

# ---------- Main Window ----------
root = tk.Tk()
root.title("Weather App")
root.geometry("400x700")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Weather App", font=FONT_TITLE, bg=BG_COLOR, fg=TEXT_COLOR)
title_label.pack(pady=(30, 5))

subtitle_label = tk.Label(root, text="Check current weather by city", font=FONT_LABEL, bg=BG_COLOR, fg=SUBTEXT_COLOR)
subtitle_label.pack(pady=(0, 20))

# Card frame
card = tk.Frame(root, bg=CARD_COLOR, padx=25, pady=25, highlightbackground="#eee0d0", highlightthickness=1)
card.pack(padx=30, fill="x")

# City input
tk.Label(card, text="City Name", font=FONT_LABEL, bg=CARD_COLOR, fg=TEXT_COLOR).pack(anchor="w")
city_entry = tk.Entry(card, font=FONT_ENTRY, bg=ENTRY_BG, fg=TEXT_COLOR,
                       insertbackground=TEXT_COLOR, relief="flat")
city_entry.pack(fill="x", ipady=6, pady=(5, 15))

# Buttons
btn_frame = tk.Frame(card, bg=CARD_COLOR)
btn_frame.pack(fill="x")

get_btn = tk.Button(btn_frame, text="Get Weather", font=FONT_LABEL, bg=ACCENT_COLOR, fg="white",
                     relief="flat", activebackground=ACCENT_DARK, command=get_weather, cursor="hand2")
get_btn.pack(side="left", expand=True, fill="x", ipady=6, padx=(0, 5))

clear_btn = tk.Button(btn_frame, text="Clear", font=FONT_LABEL, bg=ENTRY_BG, fg=TEXT_COLOR,
                       relief="flat", activebackground="#e5e0d5", command=clear_fields, cursor="hand2")
clear_btn.pack(side="left", expand=True, fill="x", ipady=6, padx=(5, 0))

# Result card
result_card = tk.Frame(root, bg=CARD_COLOR, padx=25, pady=15, highlightbackground="#eee0d0", highlightthickness=1)
result_card.pack(padx=30, pady=(25, 0), fill="x")

city_label = tk.Label(result_card, text="", font=FONT_LABEL, bg=CARD_COLOR, fg=SUBTEXT_COLOR)
city_label.pack()

emoji_label = tk.Label(result_card, text="🌡️", font=("Segoe UI", 40), bg=CARD_COLOR)
emoji_label.pack(pady=(10, 0))

temp_label = tk.Label(result_card, text="--°C", font=FONT_TEMP, bg=CARD_COLOR, fg=TEXT_COLOR)
temp_label.pack()

desc_label = tk.Label(result_card, text="Enter a city to check weather", font=FONT_DESC, bg=CARD_COLOR, fg=SUBTEXT_COLOR)
desc_label.pack(pady=(0, 10))

details_frame = tk.Frame(result_card, bg=CARD_COLOR)
details_frame.pack()

humidity_label = tk.Label(details_frame, text="", font=FONT_DETAIL, bg=CARD_COLOR, fg=SUBTEXT_COLOR)
humidity_label.pack(side="left", padx=10)

wind_label = tk.Label(details_frame, text="", font=FONT_DETAIL, bg=CARD_COLOR, fg=SUBTEXT_COLOR)
wind_label.pack(side="left", padx=10)

root.mainloop()