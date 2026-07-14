"""
BMI Calculator
Oasis Infobyte - Python Internship Project
Author: Abeer Fatima
"""

import tkinter as tk
from tkinter import messagebox

# ---------- Colors (dark theme) ----------
BG_COLOR = "#1e1e2e"
CARD_COLOR = "#2a2a3d"
ACCENT_COLOR = "#8b5cf6"
TEXT_COLOR = "#f5f5f5"
SUBTEXT_COLOR = "#a1a1aa"
ENTRY_BG = "#33334d"

FONT_TITLE = ("Segoe UI", 22, "bold")
FONT_LABEL = ("Segoe UI", 13)
FONT_ENTRY = ("Segoe UI", 13)
FONT_RESULT = ("Segoe UI", 16, "bold")
FONT_CATEGORY = ("Segoe UI", 13)


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Invalid Input", "Please enter positive numbers only.")
            return

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "#38bdf8"
        elif bmi < 25:
            category = "Normal weight"
            color = "#4ade80"
        elif bmi < 30:
            category = "Overweight"
            color = "#facc15"
        else:
            category = "Obese"
            color = "#f87171"

        result_label.config(text=f"BMI: {bmi:.2f}", fg=color)
        category_label.config(text=category, fg=color)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")


def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="BMI: --", fg=TEXT_COLOR)
    category_label.config(text="Enter your details above", fg=SUBTEXT_COLOR)


# ---------- Main Window ----------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x560")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="BMI Calculator", font=FONT_TITLE, bg=BG_COLOR, fg=TEXT_COLOR)
title_label.pack(pady=(30, 5))

subtitle_label = tk.Label(root, text="Check your Body Mass Index", font=FONT_LABEL, bg=BG_COLOR, fg=SUBTEXT_COLOR)
subtitle_label.pack(pady=(0, 20))

# Card frame
card = tk.Frame(root, bg=CARD_COLOR, padx=25, pady=25)
card.pack(padx=30, fill="both")

# Weight
tk.Label(card, text="Weight (kg)", font=FONT_LABEL, bg=CARD_COLOR, fg=TEXT_COLOR).pack(anchor="w")
weight_entry = tk.Entry(card, font=FONT_ENTRY, bg=ENTRY_BG, fg=TEXT_COLOR,
                         insertbackground=TEXT_COLOR, relief="flat")
weight_entry.pack(fill="x", ipady=6, pady=(5, 15))

# Height
tk.Label(card, text="Height (cm)", font=FONT_LABEL, bg=CARD_COLOR, fg=TEXT_COLOR).pack(anchor="w")
height_entry = tk.Entry(card, font=FONT_ENTRY, bg=ENTRY_BG, fg=TEXT_COLOR,
                         insertbackground=TEXT_COLOR, relief="flat")
height_entry.pack(fill="x", ipady=6, pady=(5, 15))

# Buttons
btn_frame = tk.Frame(card, bg=CARD_COLOR)
btn_frame.pack(fill="x", pady=(5, 0))

calc_btn = tk.Button(btn_frame, text="Calculate", font=FONT_LABEL, bg=ACCENT_COLOR, fg="white",
                      relief="flat", activebackground="#7c3aed", command=calculate_bmi, cursor="hand2")
calc_btn.pack(side="left", expand=True, fill="x", ipady=6, padx=(0, 5))

clear_btn = tk.Button(btn_frame, text="Clear", font=FONT_LABEL, bg=ENTRY_BG, fg=TEXT_COLOR,
                       relief="flat", activebackground="#44445c", command=clear_fields, cursor="hand2")
clear_btn.pack(side="left", expand=True, fill="x", ipady=6, padx=(5, 0))

# Result section
result_label = tk.Label(root, text="BMI: --", font=FONT_RESULT, bg=BG_COLOR, fg=TEXT_COLOR)
result_label.pack(pady=(25, 5))

category_label = tk.Label(root, text="Enter your details above", font=FONT_CATEGORY, bg=BG_COLOR, fg=SUBTEXT_COLOR)
category_label.pack()

root.mainloop()