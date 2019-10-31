from tkinter import *
import ctypes


window = Tk()
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
window.title("Typing Challenge")
x = str(screensize[0]//2)
xp = str(screensize[0]//4)
y = str(screensize[1]//2)
yp = str(screensize[1]//4)
window.geometry(x+"x"+y+"+"+xp+"+"+yp)


window.mainloop()
