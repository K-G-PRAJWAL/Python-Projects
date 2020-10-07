import pyautogui

# Screenshot
pyautogui.screenshot("screenshot.png")

# Image Recognition
print(pyautogui.locateOnScreen('Calc7Pic.png'))
print(pyautogui.locateCenterOnScreen('Calc7Pic.png'))
print(pyautogui.moveTo((932, 336), duration=1))
pyautogui.click(932, 336)
