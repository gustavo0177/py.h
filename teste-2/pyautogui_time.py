import pyautogui
import time
for i in range(2):
    time.sleep(4)
    posicao= pyautogui.position()
    print(f"posiçao e{posicao}")