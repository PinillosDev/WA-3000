#!/usr/bin/env python3
# Created by: pinillosdev@gmail.com

from pynput import keyboard
import pyautogui, random, threading

# isActive helps to keep active or deactivate the backgroun thread with working() function.
isActive = True

def working(): # Moves the mouse over the screen and does a scroll. No data stored.
    global isActive
    while isActive:
        pyautogui.moveTo(200, 300, duration=random.uniform(1,3))
        pyautogui.scroll(-38)
        pyautogui.moveTo(1538, 300, duration=random.uniform(1,3))
        pyautogui.scroll(-38)

def on_press(key): # Keeps tracking of the pressed keyboard character
    global isActive
    if key == keyboard.Key.esc:
        print("Task stopped...")
        isActive = False
        return False

def main():
    # Executes working() function on the background.
    mouse_thread = threading.Thread(target=working)
    mouse_thread.start()

    # "listen" the keyboard, stops when pressing 'esc'
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    mouse_thread.join()

if __name__ == "__main__":
    main()
