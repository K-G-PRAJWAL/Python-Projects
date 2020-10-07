import pyautogui

pyautogui.click(100, 100)
pyautogui.typewrite('Hello World', interval=0.2)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=0.5)
print(pyautogui.KEYBOARD_KEYS)
pyautogui.press('f5')
pyautogui.hotkey('ctrl', 's')
