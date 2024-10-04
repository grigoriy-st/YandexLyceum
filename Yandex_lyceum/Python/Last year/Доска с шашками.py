import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
canvas.create_rectangle(0, 0, 600, 600)
x1,y1 = 0, 0
x2,y2 = 75, 75
color = None
for i in range(8):
    if i < 2:
        color = 'red'
    elif i > 4:
        color = 'blue'
    if i % 2 == 0:
        for j in range(8):
            print(x1,y1,x2,y2)
            canvas.create_rectangle(x1,y1,x2,y2)
            if 2 < i < 5: 
                for i in range(8):
                    canvas.create_rectangle(x1,y1,x2,y2)
                    x1,x2 = x1 + 75, x2 + 75
                continue
            if j % 2 == 0:
                canvas.create_oval(x1,y1,x2,y2, fill=color)
            x1,x2 = x1 + 75, x2 + 75
        x1, x2 = 0, 75   
        y1,y2 = y1 + 75, y2 + 75
    else:
        for j in range(8):
            print(x1,y1,x2,y2)
            canvas.create_rectangle(x1,y1,x2,y2)
            if 2 < i < 5: 
                for i in range(8):
                    canvas.create_rectangle(x1,y1,x2,y2)
                    x1,x2 = x1 + 75, x2 + 75
                continue
            if j % 2 != 0:
                canvas.create_oval(x1,y1,x2,y2, fill=color)
            x1,x2 = x1 + 75, x2 + 75
        x1, x2 = 0, 75   
        y1,y2 = y1 + 75, y2 + 75
canvas.pack()
master.mainloop()