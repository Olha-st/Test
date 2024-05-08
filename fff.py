from tkinter import*
from random import randint
import time     # Модуль для роботи з часом і таймерами

root=Tk()
root.geometry("300x300+200+100")
root.title("Спіймай кнопку")

clicks=0        #

def b1_click():
    global clicks
    clicks += 1
    lab.config(text=str(clicks))

def clock():
    x1=randint(1,300)
    y1=randint(1,300)
    b1.place(x=x1,y=y1)
    root.after(1000, clock)

my_image=PhotoImage(file="smile.gif")
b1=Button(root, command=b1_click, image=my_image)
b1.place(x=0, y=0)
clock()

lab=Label(root, text="*", width=3, bg="blue", fg="white")
lab.pack(expand=1, anchor=NW)

root.mainloop()
