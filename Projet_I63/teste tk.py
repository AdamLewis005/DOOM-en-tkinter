"""import tkinter as tk
root = tk.Tk()

def up(event): print('up')
def dn(event): print('dn')

root.bind('<Up>', up)
root.bind('<Key-Down>', dn)
root.mainloop()

print("hello World")
"""
"""
import turtle
T = turtle.Turtle ()
k = 10
for j in range (5) :
    T.pendown ()
    T.pencolor ("red")
    for i in range (4) :
        T.fd (50 + j*k)
        T.rt (90)
    T.penup ()
    T.rt (90)
    T.bk (k/2)
    T.rt (90)
    T.fd (k/2)
    T.rt (180)
"""
"""
from tkinter import *      
root = Tk()      
canvas = Canvas(root, width = 300, height = 300,bg = "grey")      
canvas.pack()      
img = PhotoImage(file="Dottons.gif")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop() 
"""
import tkinter as tk
import time

class FPSCounter:
    def __init__(self, root):
        self.root = root
        self.frames = 0
        self.start_time = time.time()
        self.label = tk.Label(root, text="FPS: 0")
        self.label.pack()

    def update(self):
        self.frames += 1
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= 1.0:
            fps = self.frames / elapsed_time
            self.label.config(text=f"FPS: {fps:.2f}")
            self.frames = 0
            self.start_time = time.time()
        self.label.after(1, self.update)

root = tk.Tk()
fps_counter = FPSCounter(root)
fps_counter.update()
root.mainloop()