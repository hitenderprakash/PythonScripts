######################################################
# Script to calculate the MD5 and SHA256 of a string #
# provides the UI                                    #
# Author: Hitender Prakash                           #
#                                                    #
######################################################
from Tkinter import *
import hashlib

root = Tk()
root.title("MD5/SHA256 Hash Calculator")
frame = Frame(root,width=400, height=20);
frame.pack()

inputLabel = Label( root, text="Enter Hashing String:")
E1 = Entry(root, bd=1,show='*')
outputLabel = Label( root, text="MD5")
textMD5=Text(root,height=1,bd=1, width=32,state="disabled")
outputLabel2 = Label( root,text="SHA256")
textSHA256=Text(root,bd=1,height=1, width=64,state="disabled")

def doHash(event=None):
    md5 = hashlib.md5(E1.get()).hexdigest().upper()
    sha256 = hashlib.sha256(E1.get()).hexdigest()
    
    textMD5.configure(state="normal")
    textMD5.delete(1.0,END)
    textMD5.insert(INSERT,md5)
    textMD5.configure(state="disabled")
    
    textSHA256.configure(state="normal")
    textSHA256.delete(1.0,END)
    textSHA256.insert(INSERT,sha256)
    textSHA256.configure(state="disabled")

submit = Button(root, text ="Submit",command = doHash)
inputLabel.pack()
E1.pack()
E1.focus_set()
submit.pack()
outputLabel.pack()
textMD5.pack()
outputLabel2.pack()
textSHA256.pack()
root.bind('<Return>',doHash)
root.mainloop()
