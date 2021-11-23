from tkinter import *
from tkinter import messagebox
import os
import hireling

top = Tk()
top.title("Hireling Generator")

hirelingType = StringVar() 
combatant = Radiobutton(top, text = "Combatants", variable = hirelingType, value = "c")
noncombat = Radiobutton(top, text = "Non-Combatants", variable = hirelingType, value = "n")
mixed = Radiobutton(top, text = "Mixed", variable = hirelingType, value = "m")
mixed.select()

label1 = Label(top)
label1.config(text = "Type of hirelings to generate: ")
label1.pack()
combatant.pack(anchor = W)
noncombat.pack(anchor = W)
mixed.pack(anchor = W)

numFrame = Frame(top)
label2 = Label(numFrame)
label2.config(text = "Number of hirelings to generate: ")
label2.pack(side = LEFT)
hirelingNum = StringVar()
numEntry = Entry(numFrame, textvariable = hirelingNum, width = 2)
numEntry.pack(side = RIGHT)
numFrame.pack()

savepath = StringVar()
label3 = Label(top)
label3.config(text = "Location to save output: ")
label3.pack(anchor = W)
pathEntry = Entry(top, textvariable = savepath, width = 40)
pathEntry.insert(0, os.getcwd())
pathEntry.pack(anchor = W)

def makeChars():
    pathstring = str(savepath.get())
    try:
        batchSize = int(str(hirelingNum.get()))
    except:
        messagebox.showinfo("Input Error", "Type an actual number for the batch size, wise guy.")
    try:
        pathstring = os.path.join(pathstring, "output.txt")
        location = open(pathstring, "w")
        hireling.generateBatch(str(hirelingType.get()), batchSize, location)
        location.close()
        messagebox.showinfo("Success!", "Woohoo! There's a batch of new NPCs saved at the file location you specified.")
    except:
        messagebox.showinfo("Input Error", "Bad file path. Try choosing a different place to save output.")
    
    return

begin = Frame(top)
label4 = Label(begin)
label4.config(text = "Press button to generate hirelings: ")
startButton = Button(begin, text = "Generate", command = makeChars)
label4.pack(side = LEFT)
startButton.pack(side = RIGHT)
begin.pack()


top.mainloop()
