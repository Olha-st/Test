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



root.mainloop()
