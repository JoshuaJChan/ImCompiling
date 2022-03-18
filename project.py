import tkinter
import os
import subprocess
import time
from tkinter import *

window = Tk()

window.title("I'm Compiling!")
window.geometry("500x200")

elaspedTime = StringVar()
elaspedTime.set("No Compilation Done")

def inputBuildDir():
    buildDir = E.get()
    soundFile = E2.get()
    buildDir = "'" + buildDir + "'"
    buildCmd = "powershell.exe cd " + buildDir + "; make dbg.wnow64a -j8 > output.txt"
    startTime = time.time()
    os.system(buildCmd)
    endTime = time.time()
    elaspedTime.set(str(round(endTime-startTime,2)) + "s")
    L32.config(text = elaspedTime.get())
    soundCmd = "powershell.exe $PlayWav=New-Object System.Media.SoundPlayer;$PlayWav.SoundLocation=" + soundFile + "; $PlayWav.playsync()"
    os.system(soundCmd)
    os.system("notepad output.txt")

# Build Directory
F = Frame(window)
F.pack(side = TOP)

L = Label(F, text = "Build Directory",bd = 5)
L.pack(side = LEFT)

E = Entry(F,bd = 5)
E.pack(side = RIGHT)

# Sound File
F2 = Frame(window)
F2.pack(side = TOP)

L2 = Label(F2, text = "Sound File:",bd = 5)
L2.pack(side = LEFT)

E2 = Entry(F2,bd = 5)
E2.pack(side = RIGHT)

# Compile Time

F4 = Frame(window)
F4.pack(side = TOP)

L31 = Label(F4, text = "Compile time:", bd = 5)
L31.pack(side = LEFT)
L32 = Label(F4, text = elaspedTime.get(), bd = 5)
L32.pack(side = RIGHT)

# Compile Button
F3 = Frame(window)
F3.pack(side = TOP)
B = Button(F3,text="Compile!",command = inputBuildDir)
B.pack()

window.mainloop()
