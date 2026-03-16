#!/usr/bin/env python3
# Created by: pinillosdev@gmail.com

from pynput import keyboard
import pyautogui, random, threading

active = True

def working(): # Moves the mouse over the screen
    global active
    while active:
        pyautogui.moveTo(200, 300, duration=random.uniform(1,3))
        pyautogui.scroll(-38)
        pyautogui.moveTo(1538, 300, duration=random.uniform(1,3))
        pyautogui.scroll(-38)

def on_press(key): # Keeps tracking of the pressed keyboard character
    global active
    if key == keyboard.Key.esc:
        print("Task stopped...")
        active = False
        return False

def main():
    # Executes, on the background, working() function
    mouse_thread = threading.Thread(target=working)
    mouse_thread.start()

    # "listen" and "record" the keyboard, stops when pressing 'esc'
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    mouse_thread.join()

if __name__ == "__main__":
    main()
