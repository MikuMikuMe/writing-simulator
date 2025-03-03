import tkinter as tk
from tkinter import messagebox
import threading
import time
import pyautogui

def start_typing():
    # Retrieve and validate the input values.
    text = text_entry.get("1.0", tk.END).rstrip("\n")
    if not text:
        messagebox.showwarning("Input Required", "Please enter some text to type.")
        return
    try:
        initial_delay = float(initial_delay_entry.get())
        keystroke_delay = float(keystroke_delay_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for delays.")
        return

    # Disable the start button to avoid reentry while simulation runs.
    start_button.config(state=tk.DISABLED)

    def simulate_typing():
        # Wait for the starting delay to allow you to focus on the target window.
        time.sleep(initial_delay)
        # Use pyautogui.write with the interval parameter for more consistent delay.
        pyautogui.write(text, interval=keystroke_delay)
        # Re-enable the start button when finished.
        start_button.config(state=tk.NORMAL)

    # Run the simulation in a separate thread to keep the GUI responsive.
    threading.Thread(target=simulate_typing, daemon=True).start()

# Create the main window.
root = tk.Tk()
root.title("Typing Simulator")

# Text Input Field
tk.Label(root, text="Text to type:").grid(row=0, column=0, padx=5, pady=5, sticky="nw")
text_entry = tk.Text(root, width=50, height=10)
text_entry.grid(row=0, column=1, padx=5, pady=5)

# Starting Delay Input
tk.Label(root, text="Starting delay (seconds):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
initial_delay_entry = tk.Entry(root)
initial_delay_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
initial_delay_entry.insert(0, "5")  # Default value

# Keystroke Delay Input
tk.Label(root, text="Delay between keystrokes (seconds):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
keystroke_delay_entry = tk.Entry(root)
keystroke_delay_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
keystroke_delay_entry.insert(0, "0.1")  # Default value

# Start Button
start_button = tk.Button(root, text="Start Typing", command=start_typing)
start_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
