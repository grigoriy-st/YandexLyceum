import tkinter
import random as r

def draw(event):
    x1,x2 = (r.randint(0, 600), r.randint(0, 600))
    canvas.create_oval((x1,x1), (x2, x2), fill='red')
    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()