import pyautogui # click
import time # sleep
from python_imagesearch.imagesearch import imagesearch # imagesearch


'''
if an error occurs,
it eliminates the phenomenon of automatic type
'''
pyautogui.FAILSAFE = False


while True:

    # Receives coordinate values as an array
    pos = imagesearch("./findMe2.png")

    # The case of not finding and the case of finding are divided into if
    # statements
    if pos[0] == -1 and pos[1] == -1:
        print("image not found")
    else:
        print("image finds")
        pyautogui.click(pos[0], pos[1])

    # sleep
    time.sleep(1)
