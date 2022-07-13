from tkinter import *
import os
import subprocess

ws = Tk()
ws.geometry('400x300')
ws.title('Exit Page')


f = ("Times bold", 14)

def nextPage():
    ws.destroy()
    

def prevPage():
    ws.destroy()
    os.system('python3 main_screen.py')

Label(
    ws,
    text="Are you Sure to Exit?",
    padx=20,
    pady=20,
    font=f
).pack( fill=BOTH)
Label(
    ws,
    text="It will close the entire work which you did. ",
    padx=20,
    pady=20,
    font=f
).pack(fill=BOTH)
Label(
    ws,
    text="Is this really what you want to do?",
    padx=20,
    pady=20,
    font=f
).pack(fill=BOTH)
Button(
    ws, 
    text="Yes", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="No", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()