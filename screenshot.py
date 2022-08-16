import tkinter as tk
import pyscreenshot as ps
import time
from datetime import datetime
from pynput.mouse import Listener, Button
import PIL 
import cv2 as cv
import numpy as np
import pytesseract
import pyperclip

root = tk.Tk()
root.title('Screenshot Clipper')

def text_to_image():
    img = ImageGrab.grabclipboard()

   # get grayscale image
    def get_grayscale(image):
        return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    #thresholding
    def thresholding(image):
        return cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    gray = get_grayscale(img)
    thresh = thresholding(gray)

    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(thresh, config=custom_config)
    return str(text)

def get_fullscreen():
    image_name  = str(datetime.now()).replace(' ',"_").replace(':',"-")+'.png'
    root.withdraw()

    try:
        time.sleep(0.4)
        image = ps.grab()
        image.save(image_name)

    except Exception as e:
        print(e)
        return e
    root.deiconify()

def screen_area():
    image_name  = str(datetime.now()).replace(' ',"_").replace(':',"-")+'.png'
    root.withdraw()
    def on_click(x1, y1, button, pressed):
        global x0, y0

        if button == Button.left and pressed:
            x0, y0 = x1, y1

        if button == Button.left and not pressed:
            try:
                im = np.array(ps.grab(bbox=(x0, y0, x1, y1)))
                '''
                #img = cv.imread(im)
                text = tranform(im)
                print(text)
                #print(str(text))
                '''
                pyperclip.copy(im)
                print('Screenshot was taken.')
                return False
            except Exception as e:
                print(e)
                return e

        return True

        # Collect events until released
    with Listener(
            on_click=on_click) as listener:
        try:
            listener.join()
        except Exception as e:
            print(e)
            return e


    root.deiconify()


canvas = tk.Canvas(root, width = 700, height = 500)
fullScreen_button = tk.Button(text = "Clip Full Screen", command = get_fullscreen, padx = 10)
SreenArea_button = tk.Button(text = "Clip Screen Area", command =screen_area, padx = 10)
textarea = tk.Text(width = 100, height = 100, padx = 10, pady = 10, command = text_to_image) 
canvas.create_window(600, 60, window =  fullScreen_button)
canvas.create_window(600, 100, window =  SreenArea_button)
canvas.create_window(50, 10, window =  textarea)

canvas.pack()
root.mainloop()