from Tkinter import *
"#import tkinter.font"
import tkFont
import subprocess
import sys
import os
import Tkinter as tk
yc= Tk()
yc.title("sampleContacts")

import fileinput
Label(yc,text="..............click to call..............").pack()
framep = tk.Frame(yc)
framep.pack()
def closeyc():
            yc.destroy()
def call(c):
    print(c)

for l in fileinput.input('fgh'):
        l = l[0:-1]
        
        P = Button(framep, text=l, bg="bisque2", font = 'Arial 0 bold', command= lambda x=l: call(x) )
	P.pack(side=tk.TOP)
	


yc.protocol("WM_DELETE_WINDOW", closeyc)
yc.mainloop()	


