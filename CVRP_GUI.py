from tkinter import *
from tkinter.filedialog import askopenfilename
import os.path
from tkinter import messagebox


def openfile():

    filename = askopenfilename(parent=root)
    f = open(filename)
    extension = os.path.splitext(filename)[1][1:]

    if extension == '.vrp':
        return f.read()
    else:
        messagebox.showinfo("Error", "Wrong file input, please choose a vrp file")




root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()