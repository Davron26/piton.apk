from tkinter import *
import random
import time

upni = 0
downni=0
leftni=0
rightni=0
opit=0

o = random.randint(10, 490)
p = random.randint(10, 490)

def over():
    canvas.delete(ALL)
    canvas.create_text(250, 250, text='GAME OVER', fill='green', font=('Courier', 50))
    canvas.create_text(235, 300, text='Очки:', fill='green', font=('Courier', 30))
    canvas.create_text(310, 300, text=opit, fill='green', font=('Courier', 30))

def move_up(self):
    canvas.itemconfig(mytriangle, image=my_up)
    global upni, downni, leftni, rightni
    upni = 1
    downni = 0
    leftni = 0
    rightni = 0


def move_down(self):
    canvas.itemconfig(mytriangle, image=my_down)
    global upni, downni, leftni, rightni
    upni = 0
    downni = 1
    leftni = 0
    rightni = 0


def move_left(self):
    canvas.itemconfig(mytriangle, image=my_left)
    global upni, downni, leftni, rightni
    upni = 0
    downni = 0
    leftni = 1
    rightni = 0


def move_right(self):
    canvas.itemconfig(mytriangle, image=my_right)
    global upni, downni, leftni, rightni
    upni = 0
    downni = 0
    leftni = 0
    rightni = 1


tk = Tk()
canvas = Canvas(tk, width=500, height=500, highlightthickness=0)
canvas.pack()
bg = PhotoImage(file="background.gif")
w = bg.width()
h = bg.height()
for x in range(0, 5):
    for y in range(0, 5):
        canvas.create_image(x * w, y * h, \
                            image=bg, anchor='nw')
my_up = PhotoImage(file="figure-up.gif")
my_right = PhotoImage(file="figure-right.gif")
my_left = PhotoImage(file="figure-left.gif")
my_down = PhotoImage(file="figure-down.gif")

i_tem = PhotoImage(file="item.gif")
item = canvas.create_image(o, p, anchor=NW, image=i_tem)

mytriangle = canvas.create_image(250, 250, anchor=NW, image=my_up)
ochko1=canvas.create_text(20,10,text="Очки:",fill="white")
ochko=canvas.create_text(45,10,text=opit,fill="white")

hasItem = True

while (1):
    try:
        if canvas.coords(mytriangle)[0] >= 485:
            over()
        elif canvas.coords(mytriangle)[0] <= -10:
            over()
        elif canvas.coords(mytriangle)[1] >= 485:
            over()
        elif canvas.coords(mytriangle)[1] <= -15:
            over()
    except IndexError:
        pass

    if upni == 1:
        canvas.move(mytriangle, 0, -5)
    if downni == 1:
        canvas.move(mytriangle, 0, 5)
    if leftni == 1:
        canvas.move(mytriangle, -5, 0)
    if rightni == 1:
        canvas.move(mytriangle, 5, 0)

    if (hasItem):
        try:
            x1, y1 = canvas.coords(item)
            x2, y2 = canvas.coords(mytriangle)
        except ValueError:
            pass
        x2 += 8;
        y2 += 6
        if (abs(x1 - x2) < 5) and (abs(y1 - y2) < 5):
            #hasItem = False
            opit+=1
            canvas.delete(ochko)
            ochko=canvas.create_text(45,10,text=opit,fill="white")
            o = random.randint(10, 490)
            p = random.randint(10, 490)
            canvas.coords(item, o, p)

    #print(canvas.coords(mytriangle))
    #print(canvas.coords(item))
    tk.update()
    time.sleep(0.01)
    canvas.bind_all('<KeyPress-Up>', move_up)
    canvas.bind_all('<KeyPress-Down>', move_down)
    canvas.bind_all('<KeyPress-Left>', move_left)
    canvas.bind_all('<KeyPress-Right>', move_right)
    time.sleep(0.01)
