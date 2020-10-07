import pyautogui

# print(pyautogui.size())
# print(pyautogui.position())
# pyautogui.moveTo(10, 10, duration=1.5)
# pyautogui.moveRel(200, 10, duration=1.5)
# pyautogui.displayMousePosition()

# MS Paint
pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.1)
    distance -= 25
    pyautogui.dragRel(0, distance, duration=0.1)
    pyautogui.dragRel(-distance, 0, duration=0.1)
    distance -= 25
    pyautogui.dragRel(0, -distance, duration=0.1)
