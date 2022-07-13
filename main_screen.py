# Reference: https://stackoverflow.com/questions/65465312/how-to-display-image-with-upload-button-in-and-resize-it-with-window-resize-dyn
from pydoc import text
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import PIL
import os
import subprocess
from tkinter import filedialog

root = tk.Tk()
root.title("Image Memory Archive")
root.geometry('1200x900')
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)
frame_drink = LabelFrame(root, text = "Record your memory. Note: When you make changes in your memo, you need to save the memo!")
frame_drink.pack(side="right", fill="both", expand=True)

class Layout:
    
    def __init__(self,master):
        self.master = master
        self.rootgeometry()
        self.counter = 0
        self.button = Button(frame_burger, text='Upload Image File', command=self.loadbackground)
        self.button.pack(side = "bottom")
        
        self.button2 = Button(frame_drink, text ='Upload Text file', command = self.loadmemo)
        self.button2.pack(side = "bottom")
        self.button3 = Button(frame_burger, text = 'Undo the image upload', command = self.clear_label_image)
        self.button3.pack(side = "top")
        
        self.text = None

        self.button4 = Button(frame_drink, text = 'Undo the Writings', command = self.undo_text)
        self.button4.pack(side = "top")

        self.button5 = Button(frame_burger, text = "Save Image", command = self.save_imag)
        self.button5.pack(side = "left")

        self.button6 = Button(frame_drink, text = "Save Memo", command = self.save_txt)
        self.button6.pack(side = "left")

        self.button7 = Button(self.master, text= "FAQs", command = self.FAQ)
        self.button7.pack(side = "top")

        self.button8 = Button(self.master, text="Exit", command = self.exit_page)
        self.button8.pack(side="top")
       
        self.canvas = tk.Canvas(self.master)
        self.canvas.pack(fill=BOTH, expand=True)
    
        self.background_image = None
        self.image_copy = None
        self.background = None
        self.filename = None
        self.textfile = None
        self.label = tk.Label(frame_burger)
        self.label.pack(fill='both', expand=True)
        self.img_counter = 0
        
    def loadmemo(self):
        text_file = filedialog.askopenfilename()
        self.textfile = text_file
        if self.counter == 0:
            text_file = open(text_file, 'r')
        stuff = text_file.read()
        self.text = Text(frame_drink, undo= True)
        self.text.pack(side="right",expand=True, fill=BOTH)
        
        self.text.insert(END, stuff)
        text_file.close()
        self.counter = self.counter + 1

    def loadbackground(self):

        self.background_image = Image.open(self.openfn())
        self.image_copy = self.background_image.copy()
        
        self.background = ImageTk.PhotoImage(self.background_image.resize((self.canvas.winfo_width(), self.canvas.winfo_height())))
        self.label.configure(image=self.background)
        self.label.bind('<Configure>',self.resizeimage)

    def openfn(self):
        filename = filedialog.askopenfilename(title='open')
        self.filename = filename
        return filename
    

    def rootgeometry(self):
        x=int(self.master.winfo_screenwidth()*0.8)
        y=int(self.master.winfo_screenheight()*0.7)
        z = str(x) +'x'+str(y)
        self.master.geometry(z)

    def resizeimage(self,event):
        W = int(event.width * 0.9)
        image = self.image_copy.resize((event.width, event.height))
        self.image1 = ImageTk.PhotoImage(image)

    def clear_label_image(self):
        self.background= None
    
    def undo_text(self):
        self.text.edit_undo()
    
    
    def save_imag(self):
        
       picture = Image.open(self.filename)  
     
       picture = picture.save("image.jpeg", "JPEG")
       self.img_counter = self.img_counter + 1
    def save_txt(self):
        text = self.text
        text_file = open("test.txt", "w")
        text_file.write(text.get(1.0, END))
        text_file.close()
    
    def exit_page(self):
        root.destroy()
        os.system("python3 exit.py")
        self.save_imag
        self.save_txt
        self.loadbackground
        self.loadmemo
        
    
    def FAQ(self):
        root.destroy()
        os.system('python3 FAQs.py')
       
a = Layout(root)
root.mainloop()

