from tkinter import *
from tkinter import messagebox
import os
import hireling

top = Tk()
top.title("Hireling Generator")

buttons_frame = Frame(top)

combat_type_frame = Frame(buttons_frame)
hirelingType = StringVar() 
combatant = Radiobutton(combat_type_frame, text = "Combatants", variable = hirelingType, value = "c")
noncombat = Radiobutton(combat_type_frame, text = "Non-Combatants", variable = hirelingType, value = "n")
mixed = Radiobutton(combat_type_frame, text = "Mixed", variable = hirelingType, value = "m")
mixed.select()
label1 = Label(combat_type_frame)
label1.config(text = "Type of hirelings to generate: ")
label1.pack()
combatant.pack()
noncombat.pack()
mixed.pack()
combat_type_frame.pack(side = LEFT)

name_culture_frame = Frame(buttons_frame)
culture_label = Label(name_culture_frame)
culture_label.config(text = "Type of names to use: ")
culture_label.pack()
culture = StringVar()
no_culture = Radiobutton(name_culture_frame, text = "None", variable = culture, value = "none")
no_culture.select()
midlander = Radiobutton(name_culture_frame, text = "Midlander", variable = culture, value = "m")
karok = Radiobutton(name_culture_frame, text = "Karok", variable = culture, value = "k")
nydissian = Radiobutton(name_culture_frame, text = "Nydissian", variable = culture, value = "n")
varnori = Radiobutton(name_culture_frame, text = "Varnori", variable = culture, value = "v")
random = Radiobutton(name_culture_frame, text = "Mixed", variable = culture, value = "r")
no_culture.pack()
midlander.pack()
karok.pack()
nydissian.pack()
varnori.pack()
random.pack()
name_culture_frame.pack(side = RIGHT)

buttons_frame.pack()

numFrame = Frame(top)
label2 = Label(numFrame)
label2.config(text = "Number of hirelings to generate: ")
label2.pack(side = LEFT)
hirelingNum = StringVar()
numEntry = Entry(numFrame, textvariable = hirelingNum, width = 2)
numEntry.insert(0, "10")
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
        return
    try:
        pathstring = os.path.join(pathstring, "output.txt")
        location = open(pathstring, "w")
        hireling.generateBatch(str(hirelingType.get()), batchSize, location, str(culture.get()))
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
