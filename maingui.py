from Tkinter import *
import tkFont
from PIL import ImageTk,Image
import Tkinter as tk
import sys
import os
import subprocess
import fileinput 
### GUI DEFINITIONS ###
win = Tk()
win.title("PHONE AUTO")

### Event Functions ###
def CONNECT():
	#call bash code for bluetooth
    
    subprocess.call('./bluetooth_connection', shell=True)
    popup = Toplevel()
    popup.title("Search")
    def closepopup():
            popup.destroy()
    def pair(n):
        command='./pair_to '+str(n)
        subprocess.call(command, shell=True)
        B0["text"] ="CONNECTED"
        popup.destroy()
    #take the num of devices
    i=0
    for l in fileinput.input('devname'):
            l = l[0:-1]
            P = Button(popup, text=l, bg="bisque2", font = 'Arial 0 bold', command= lambda j=i+1: pair(j))
            P.pack(side=tk.TOP)
            i=i+1
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()
    
def contact():
	os.system('python contactlist.py')
        
def Answercall():
	os.system('python ./ofono-1.18/test/answer-calls')

def Hangupcall():
	os.system('python ./ofono-1.18/test/hangup-all')

def close():
        win.destroy()

### WIDGETS ###

# Button

Label(win,text="..............WELCOME TO PHONE AUTO..............").pack()
frame = tk.Frame(win)
frame.pack()
#path for image
path = 'ab.jpg'
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(frame, image = img)
panel.pack(side = "right", fill = "both", expand = "yes")

B0 = Button(frame, text ="CONNECT", font = 'Arial 0 bold', command=CONNECT)
B0.pack()
B1 = Button(frame,text="Contact", font = 'Arial 0 bold', command=contact)
B1.pack()
B2 = Button(frame,text="Answer call", font = 'Arial 0 bold', command=Answercall)
B2.pack()
B3 = Button(frame,text="Hang up", font = 'Arial 0 bold', command=Hangupcall)
B3.pack()


exitButton = Button(frame, text='Exit', font='Arial 0 bold', command=close, bg='red').pack()

win.protocol("WM_DELETE_WINDOW", close) 

win.mainloop() # Loops forever
