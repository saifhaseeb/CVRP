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

    def getGridSize():

        flag = False
        i = 0
        k = len(content)
        largestnumberArray = []

        while not flag:
            while i < k:

                if content[i] == 'EOF':
                    flag = True

                if content[i][0].isdigit():
                    largestnumber = findLargestNumber(content[i])
                    largestnumberArray.append(largestnumber)
                    i += 1

                else:
                    i += 1

            largestCoordinate = max(largestnumberArray)

        x = 0

        if largestCoordinate < 10000:
            x = 10000

        if largestCoordinate < 1000:
            x = 1000

        if largestCoordinate > 100:
            x = 100

        return x

    def createGrid():

        x = [['.' for i in range(getGridSize())] for j in range(getGridSize())]
        return x




root = Tk()
b = Button(root, text="Open VRP File", command=openFile)
b.pack()
root.mainloop()