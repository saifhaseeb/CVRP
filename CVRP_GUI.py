import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os.path


def openfile():

    filename = askopenfilename(parent=root)
    extension = os.path.splitext(filename)[1][1:]

    if extension == '':
        messagebox.showinfo("Error", "Wrong file input, please choose a vrp file")

    else:
        with open(filename) as f:
            content = f.readlines()

        content = [x.strip() for x in content]
        print(content)



root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()