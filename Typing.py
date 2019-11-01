from tkinter import *
import ctypes

#Creating window and Customizing it
window = Tk()
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
window.title("Typing Challenge")
x = screensize[0]//2
xp = screensize[0]//4
y = screensize[1]//2
yp = screensize[1]//4
window.geometry("{}x{}+{}+{}".format(x,y,xp,yp))
window.grid_columnconfigure(0,weight=1)
window.grid_rowconfigure(2,weight = 1)

#Creating a Frame and inserting Text widgit and making it Scroll
textScreen = Frame(window,width = xp-200,height = yp-200,pady = 5,padx = 5)
textScreen.grid(row = 0)
screen = Text(textScreen,height = yp-200,width = xp-200)
scrollbar = Scrollbar(textScreen)
scrollbar.config(command=screen.yview)
screen.config(yscrollcommand = Scrollbar.set)
scrollbar.pack(side = RIGHT,fill = Y)
screen.pack(expand = YES,fill = BOTH)
screen.insert(END,"Just\nhai\nhello\nand")

#Creating Frame for typing Entry and button to start
typeScreen = Frame(window,width = 100,height = 10,pady = 5,padx = 5)
typeScreen.grid(row = 1)
type = Entry(typeScreen,width = 40,exportselection=0)
type.pack(padx =100,pady=50,expand=1,fill='x')
start = Button(typeScreen,width = 30,text = "Start")
start.pack()

window.mainloop()
