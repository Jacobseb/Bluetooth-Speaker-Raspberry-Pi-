from Tkinter import *
"#import tkinter.font"
import tkFont
import subprocess
import sys
import os
import Tkinter as tk
import fileinput
yc= Tk()
yc.title("Your Contacts")

cnv = Canvas(yc)
cnv.grid(row=0, column=0, sticky='nswe')
frm = Frame(cnv)

Label(frm,text="..............click to call..............").pack()

vScroll = Scrollbar(yc, orient=VERTICAL, command=cnv.yview)
vScroll.grid(row=0, column=1, sticky='ns')
cnv.configure(yscrollcommand=vScroll.set)
cnv.create_window(0, 0, window=frm, anchor='nw')

def closeyc():
            yc.destroy()
def call(c):
    print(c)
    command='./call '+str(c)
    subprocess.call(command, shell=True)  
    yc.destroy()  
#

for l in fileinput.input('contactname'):
        l = l[0:-1] 
    	P = Button(frm, text=l, bg="bisque2", font = 'Arial 0 bold', command= lambda x=l: call(x) )
	P.pack(side=tk.TOP,padx=2, pady=2)

frm.update_idletasks()
cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
yc.protocol("WM_DELETE_ycDOW", closeyc)
yc.mainloop()	

