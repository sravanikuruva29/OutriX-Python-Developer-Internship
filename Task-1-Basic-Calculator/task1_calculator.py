"""
OutriX Python Developer Internship - Task 1
Basic Calculator with GUI
Tools: Python, Tkinter

Run:
    python task1_calculator.py
"""

import tkinter as tk
from tkinter import messagebox


def calculate(operation):
    try:
        a = float(first_entry.get())
        b = float(second_entry.get())

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                raise ZeroDivisionError
            result = a / b

        result_var.set(f"Result: {result:g}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")


def clear():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    result_var.set("Result: ")


root = tk.Tk()
root.title("OutriX - Basic Calculator")
root.geometry("420x330")
root.resizable(False, False)

tk.Label(
    root,
    text="Basic Calculator",
    font=("Arial", 20, "bold")
).pack(pady=15)

form = tk.Frame(root)
form.pack(pady=5)

tk.Label(form, text="First Number:", font=("Arial", 11)).grid(
    row=0, column=0, padx=10, pady=8, sticky="e"
)
first_entry = tk.Entry(form, width=22, font=("Arial", 12))
first_entry.grid(row=0, column=1, padx=10, pady=8)

tk.Label(form, text="Second Number:", font=("Arial", 11)).grid(
    row=1, column=0, padx=10, pady=8, sticky="e"
)
second_entry = tk.Entry(form, width=22, font=("Arial", 12))
second_entry.grid(row=1, column=1, padx=10, pady=8)

buttons = tk.Frame(root)
buttons.pack(pady=15)

for i, (symbol, text) in enumerate([
    ("+", "Add"),
    ("-", "Subtract"),
    ("*", "Multiply"),
    ("/", "Divide")
]):
    tk.Button(
        buttons,
        text=text,
        width=11,
        command=lambda op=symbol: calculate(op)
    ).grid(row=0, column=i, padx=3)

result_var = tk.StringVar(value="Result: ")
tk.Label(
    root,
    textvariable=result_var,
    font=("Arial", 14, "bold")
).pack(pady=10)

tk.Button(
    root,
    text="Clear",
    width=12,
    command=clear
).pack(pady=5)

root.mainloop()
