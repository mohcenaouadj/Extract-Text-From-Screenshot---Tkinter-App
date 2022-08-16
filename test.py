
import tkinter as tk
from pynput.mouse import Listener
from PIL import Image, ImageGrab
import pyscreenshot as ps
import time
from datetime import datetime

root = tk.Tk(className = 'Screenshot')

canvas = tk.Canvas(root,  width = 500, height = 300)
user_left = tk.Entry(root, text = '0')

image_name =str(datetime.now()).replace(" ","-").replace(":","-")+".png"

def on_move(x, y):
    print('Pointer moved to {0}'.format( (x, y) ))

def on_clik(x, y, button, pressed):
    global ix, iy
    if button == button.left:
        if pressed:
            ix = x
            iy = y

            print('left button pressed at {0}'.format((x,y)))
        else:
            
            print('left button released at {0}'.format((x,y)))
            Canvas.create_rectangle(ix, iy, x, y, outline="red", width = 5)
            Canvas.pack()
            img = ImageGrab.grab(bbox = (ix, iy, x, y)) 
            img.save(image_name)
            root.quit()

    if not pressed:
        # Stop listener
        return False

print(screen_width, screen_height)


root_geometry = str(screen_width) + 'x' + str(screen_height) #Creates a geometric string argument
root.geometry(root_geometry) #Sets the geometry string value

root.overrideredirect(True)
root.wait_visibility(root)
root.wm_attributes("-alpha", 0.3)#Set windows transparent

canvas = tk.Canvas(root, width=screen_width, height=screen_height)#Crate canvas
canvas.config(cursor="cross")#Change mouse pointer to cross
canvas.pack()



with Listener(on_move=on_move, on_click=on_click) as listener:
    root.mainloop()#Start tkinter window
    listener.join()