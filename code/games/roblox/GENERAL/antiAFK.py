import time
from pynput.keyboard import Controller

# CONFIG
TIME = 10 # TIME IN MINUTES

keyboard = Controller()

def press_keys():
  
    keyboard.press('q')
    print("Holding Q")
    time.sleep(0.5)
    keyboard.release('q')
    print("Released Q")

    time.sleep(0.5)

    keyboard.press('e')
    print("Holding E")
    time.sleep(0.5)
    keyboard.release('e')
    print("Released E")

if __name__ == "__main__":
    while True:
        press_keys()
        print("Waiting", TIME,  "minutes...")
        time.sleep(TIME * 60)