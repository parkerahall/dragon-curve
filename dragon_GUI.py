#!/usr/bin/env python

"""
    GUI for dragon curve visualization
"""

import Tkinter as tk
from dragon import dragon

"""
Enables run button if all fields are filled
"""
def check_fields(*args):
    is_filled = all([var.get() for var in FIELD_VARS])
    if is_filled:
        run_button.config(state=tk.NORMAL)
    else:
        run_button.config(state=tk.DISABLED)

"""
Draws dragon curve based on input fields
"""
def run_dragon(*args):
    args = [int(var.get()) for var in FIELD_VARS]
    dragon(args[0], args[1], args[2])

root = tk.Tk()
root.title("Dragon Curve GUI")

frame = tk.Frame(root)

FIELD_VARS = []
NUM_FIELDS = 3

for i in range(NUM_FIELDS):
    new_var = tk.StringVar(frame)
    new_var.trace("w", check_fields)
    FIELD_VARS.append(new_var)

iter_label = tk.Label(frame, text="Iterations")
iter_entry = tk.Entry(frame, textvariable=FIELD_VARS[0])
iter_label.grid(row=0, column=0)
iter_entry.grid(row=0, column=1)

size_label = tk.Label(frame, text="Square size")
size_entry = tk.Entry(frame, textvariable=FIELD_VARS[1])
size_label.grid(row=1, column=0)
size_entry.grid(row=1, column=1)

speed_label = tk.Label(frame, text="Draw speed")
speed_entry = tk.Entry(frame, textvariable=FIELD_VARS[2])
speed_label.grid(row=2, column=0)
speed_entry.grid(row=2, column=1)

run_button = tk.Button(frame, text="Run", state=tk.DISABLED, command=run_dragon)
run_button.grid(row=3, column=1)

frame.pack()

root.mainloop()