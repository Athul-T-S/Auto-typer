import pyperclip
import pyautogui
import keyboard
import time

def type_clipboard_content():
    # Get clipboard content
    text = pyperclip.paste()

    if not text:
        print("Clipboard is empty.")
        return

    print("Typing started...")
    time.sleep(1)  # time to switch to target window

    # Paste each character precisely
    for char in text:
        if char == '\n':
            pyautogui.press('enter')
        else:
            pyautogui.write(char)
        time.sleep(0.005)  # smooth typing, adjustable

    print("Typing finished.")

# Hotkey to trigger typing
keyboard.add_hotkey("ctrl+alt+t", type_clipboard_content)

print("AutoTyper is running. Copy some text, then press Ctrl+Alt+T.")
keyboard.wait()





