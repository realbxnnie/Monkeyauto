import pyautogui
import time

class Monkeyauto:
    def __init__(self):
        message = input("Enter message to type: ")
        interval = float(input("Enter interval of typing (the best: 0.03):"))

        print("Please open monkeytype. Typing will start in 3 seconds")

        time.sleep(3)

        pyautogui.write(message, interval)

if __name__ == "__main__":
    program = Monkeyauto()
