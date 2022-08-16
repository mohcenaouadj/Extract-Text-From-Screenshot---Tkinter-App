
import tkinter as tk
#from pynput.mouse import Listener
import pyscreenshot as ps
import time
from datetime import datetime
#import turtle

root = tk.Tk(className = 'Screenshot')

canvas = tk.Canvas(root,  width = 500, height = 300)
#user_left = tk.Entry(root, text = '0')

image_name =str(datetime.now()).replace(" ","-").replace(":","-")+".png"



#root.geometry('500x200')
def get_fullscreen():
  root.withdraw()
  try:
    time.sleep(0.4)
    print('Button hass been clicked')
    image = ps.grab()
    image.save(image_name)
  except Exception as e:
    print(e)
    return e

  root.deiconify()



canvas.pack()
root.mainloop()

