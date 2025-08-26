import cv2
import numpy as np
import mss
from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyController
import time

# Screen config
monitor = {"top": 550, "left": 3000, "width": 200, "height": 340}


# Input Setup
fish_count = 0
last_fish_time = time.time()
start_time = time.time()
mouse = Controller()
keyboard = KeyController()
clicking = False

# Color detection via the gray arrow
arrow_visible_last_frame = False
activated_this_fish = False

# Color Ranges
# If the color detection doesn't work properly you might have to adjust the colors
LOWER_WHITE_BGR = np.array([180, 180, 180])
UPPER_WHITE_BGR = np.array([255, 255, 255])

LOWER_ARROW_BGR = np.array([210, 196, 153])
UPPER_ARROW_BGR = np.array([250, 236, 193])

# Clicking for catching the fish (press_ mouse and release_mouse function)
def press_mouse():
    global clicking
    if not clicking:
        mouse.press(Button.left)
        clicking = True

def release_mouse():
    global clicking
    if clicking:
        mouse.release(Button.left)
        clicking = False


# Main loop
with mss.mss() as sct:
    while True:
        frame = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        # Masks
        white_mask = cv2.inRange(frame, LOWER_WHITE_BGR, UPPER_WHITE_BGR)
        arrow_mask = cv2.inRange(frame, LOWER_ARROW_BGR, UPPER_ARROW_BGR)

        # Contours
        white_contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        arrow_contours, _ = cv2.findContours(arrow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find white bar
        white_center_y = None
        if white_contours:
            white_cnt = max(white_contours, key=cv2.contourArea)
            wx, wy, ww, wh = cv2.boundingRect(white_cnt)
            white_center_y = wy + wh // 2
            cv2.rectangle(frame, (wx, wy), (wx + ww, wy + wh), (255, 0, 0), 2)

        # Find arrow
        arrow_center_y = None
        if arrow_contours:
            arrow_cnt = max(arrow_contours, key=cv2.contourArea)
            ax, ay, aw, ah = cv2.boundingRect(arrow_cnt)
            arrow_center_y = ay + ah // 2
            cv2.rectangle(frame, (ax, ay), (ax + aw, ay + ah), (0, 0, 255), 2)

        # Fish caught detection
        arrow_visible_now = arrow_center_y is not None

        if arrow_visible_last_frame and not arrow_visible_now and not activated_this_fish:
            fish_count += 1
            last_fish_time = time.time()
            elapsed = last_fish_time - start_time
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            print(f"🎣 Fish caught! Total: {fish_count} in {minutes}m {seconds}s")
            keyboard.press('8')
            keyboard.release('8')
            time.sleep(1)
            mouse.click(Button.left)
            time.sleep(3)
            mouse.click(Button.left)
            activated_this_fish = True

        # Failsafe
        if not arrow_visible_now and (time.time() - last_fish_time > 15):
            print("⏱️ Timeout — Recasting...")
            keyboard.press('8')
            keyboard.release('8')
            time.sleep(1)
            mouse.click(Button.left)
            time.sleep(3)
            mouse.click(Button.left)
            last_fish_time = time.time()
            activated_this_fish = True

        # Regular control logic
        if white_center_y is not None and arrow_center_y is not None:
            tolerance = 25  # Make the window bigger to act sooner
            lower_bound = arrow_center_y - tolerance
            upper_bound = arrow_center_y + tolerance

            if white_center_y < lower_bound:
                release_mouse()
            elif white_center_y > upper_bound:
                press_mouse()
            else:
                release_mouse()
        else:
            release_mouse()



        # Reset state for next fish
        if arrow_visible_now:
            activated_this_fish = False

        arrow_visible_last_frame = arrow_visible_now

        # Show debug view
        cv2.imshow("Fishing Bot (Arrow Tracking)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

release_mouse()
cv2.destroyAllWindows()
