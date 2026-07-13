"""
Random Password Generator
Oasis Infobyte - Python Internship Project 3
Author: Abeer Fatima
"""

import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Too Short", "Password length should be at least 4.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")
        return

    char_pool = ""
    if use_letters.get():
        char_pool += string.ascii_letters
    if use_numbers.get():
        char_pool += string.digits
    if use_symbols.get():
        char_pool += string.punctuation

    if not char_pool:
        messagebox.showwarning("No Character Type Selected", "Select at least one character type.")
        return

    password = "".join(random.choice(char_pool) for _ in range(length))

    result_var.set(password)


def copy_to_clipboard():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Nothing to Copy", "Generate a password first.")


# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("420x520")
root.configure(bg="#1e1e2e")
root.resizable(True, True)

FONT = ("Segoe UI", 12)
BG = "#1e1e2e"
FG = "#f5f5f5"
ACCENT = "#a78bfa"

title_label = tk.Label(root, text="Password Generator", font=("Segoe UI", 18, "bold"), bg=BG, fg=ACCENT)
title_label.pack(pady=20)

length_frame = tk.Frame(root, bg=BG)
length_frame.pack(pady=10)

tk.Label(length_frame, text="Password Length:", font=FONT, bg=BG, fg=FG).pack(side="left", padx=5)
length_entry = tk.Entry(length_frame, font=FONT, width=5, justify="center")
length_entry.insert(0, "12")
length_entry.pack(side="left")

use_letters = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

options_frame = tk.Frame(root, bg=BG)
options_frame.pack(pady=10)

tk.Checkbutton(options_frame, text="Letters (a-z, A-Z)", variable=use_letters,
               font=FONT, bg=BG, fg=FG, selectcolor=BG, activebackground=BG).pack(anchor="w")
tk.Checkbutton(options_frame, text="Numbers (0-9)", variable=use_numbers,
               font=FONT, bg=BG, fg=FG, selectcolor=BG, activebackground=BG).pack(anchor="w")
tk.Checkbutton(options_frame, text="Symbols (!@#$...)", variable=use_symbols,
               font=FONT, bg=BG, fg=FG, selectcolor=BG, activebackground=BG).pack(anchor="w")

generate_btn = tk.Button(root, text="Generate Password", font=("Segoe UI", 12, "bold"),
                          bg=ACCENT, fg="#1e1e2e", activebackground="#8b5cf6",
                          relief="flat", padx=10, pady=8, command=generate_password)
generate_btn.pack(pady=20)

result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Consolas", 13),
                         justify="center", width=28, relief="flat")
result_entry.pack(pady=5, ipady=6)

copy_btn = tk.Button(root, text="Copy to Clipboard", font=FONT,
                      bg="#313244", fg=FG, activebackground="#45475a",
                      relief="flat", padx=10, pady=6, command=copy_to_clipboard)
copy_btn.pack(pady=15)

root.mainloop()