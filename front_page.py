from re import L
from tkinter import *
import os
import sys
import subprocess
ws = Tk()
ws.geometry('1500x1200')
ws.title('PythonGuides')

v = StringVar()


f = ("Times bold", 30)

def nextPage():
   ws.destroy()
   os.system('python3 tutorial.py')

def prevPage():
    ws.destroy()
    os.system('python3 main_screen.py')
    #import main_screen
    #ws.destroy()
label1 = Label(ws, font= f)
label2 = Label(ws, font = f, textvariable= v)
label3 = Label(ws, font=f)
label4 = Label(ws, font=f)

label1['text'] = 'Welcome to Image Memory Archive!'
v.set('You can go directly to the program or go to Instruction session before using the program.')
label3['text'] = '<Cuation>'
label4['text'] = 'FAQ and Exit buttons reset all of your works. Save all of your works before pressing Exit or FAQ!'
label1.pack(expand=True, fill=BOTH)
label2.pack(expand=True, fill=BOTH)
label3.pack(expand=True, fill=BOTH)
label4.pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Go to Instructions", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="Go to Main", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()