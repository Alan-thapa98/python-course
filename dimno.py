import time
import pyautogui
from PIL import Image, ImageGrab
from numpy import asarray


def hit(key):
    pyautogui.KeyDown(key)


# while True:
#     pyautogui.keyDown('A')
#     pyautogui.keyDown('l')
#     pyautogui.keyDown('a')
#     pyautogui.keyDown('n')
#     pyautogui.keyDown('Thapa')

def takescreenshot():
    image = ImageGrab.grab().convert('L')


# def drow():


if __name__ == "__main__":
    time.sleep(2)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        data
    image = takescreenshot()
    print(asarray(image))
    for i in range(34, 45):
        for j in range(45, 67):
            data[i, j] = 0

    image.show()
