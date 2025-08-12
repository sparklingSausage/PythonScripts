import pyautogui
import time

print("Move your mouse to the TOP-LEFT corner of the green zone area...")
time.sleep(3)
x1, y1 = pyautogui.position()
print(f"Top-left corner: x={x1}, y={y1}")

print("Now move your mouse to the BOTTOM-RIGHT corner of the green zone area...")
time.sleep(5)
x2, y2 = pyautogui.position()
print(f"Bottom-right corner: x={x2}, y={y2}")

width = x2 - x1
height = y2 - y1

print(f"\nUse this in your script:\nmonitor = {{'top': {y1}, 'left': {x1}, 'width': {width}, 'height': {height}}}")
