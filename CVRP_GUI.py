import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os.path

def getNum(text):
    return int(''.join(ele for ele in text if ele.isdigit() or ele == '.'))

def findLargestNumber(text):
    ls = list()
    for w in text.split():
        try:
            ls.append(int(w))
        except:
            pass
    try:
        return max(ls)
    except:
        return None

def openFile():

    filename = askopenfilename(parent=root)
    extension = os.path.splitext(filename)[1][1:]

    if extension == '':
        messagebox.showinfo("Error", "No file chosen, please click on a valid test file")

    else:
        with open(filename) as f:
            content = f.readlines()

        content = [x.strip() for x in content]
        print(content)
        totalnode = getNum(content[3])
        print(totalnode)

    def getCoordinates():

        flag = False

        i = 0
        k = len(content)
        largestnumberArray = []

        while not flag:
            while i < k:

                if content[i][0].isdigit():
                    largestnumber = findLargestNumber(content[i])
                    largestnumberArray.append(largestnumber)
                    i += 1

                else:
                    i += 1

            return max(largestnumberArray)



root = Tk()
b = Button(root, text="Open VRP File", command=openFile)
b.pack()
root.mainloop()