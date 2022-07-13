from tkinter import *
import os
import subprocess
ws = Tk()
ws.geometry('1200x900')
ws.title('FAQs')


f = ("Times bold", 14)

def nextPage():
    import email
    

def prevPage():
    ws.destroy()
    os.system('python3 main_screen.py')
    #import main_screen
    #ws.destroy()
  
Label(
    ws,
    text="This is a FAQ page",
    padx=20,
    pady=20,
    #bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="More Questions? Send Email to Us!", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="Return to Main", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()