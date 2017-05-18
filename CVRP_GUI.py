import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os.path

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit() or ele == '.'))

def openFile():

    filename = askopenfilename(parent=root)
    extension = os.path.splitext(filename)[1][1:]

    if extension == '':
        messagebox.showinfo("Error", "No file chosen, please click on a valid test file")

    else:
        with open(filename) as f:
            content = f.readlines()

        content = [x.strip() for x in content]
        totalnode = getNum(content[3])




root = Tk()
b = Button(root, text="Open VRP File", command=openFile)
b.pack()
root.mainloop()