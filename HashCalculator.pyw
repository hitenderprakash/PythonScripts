######################################################
# Script to calculate the MD5 and SHA256 of a string #
# provides the UI                                    #
# Author: Hitender Prakash                           #
#                                                    #
######################################################
from Tkinter import *
import hashlib
#import base64

root = Tk()
root.title("Hash Calculator")

inputLabel = Label( root, text="Enter input String:")
inputEntry = Entry(root, bd=1,show='*')

md5Label = Label( root, text="MD5")
textMD5=Text(root,height=1,bd=1, width=32,state="disabled")

sha1Label = Label( root,text="SHA1")
textSHA1=Text(root,bd=1,height=1, width=40,state="disabled")

sha256Label = Label( root,text="SHA256")
textSHA256=Text(root,bd=1,height=1, width=64,state="disabled")
'''
base64EncodeLabel = Label( root,text="base64 Encode")
textBase64Encode = Text(root,bd=1,height=1,width=64,state="disabled")
'''

def doHash(event=None):
    inputVal=inputEntry.get()
    
    md5 = hashlib.md5(inputVal).hexdigest().upper()
    sha1 =  hashlib.sha1(inputVal).hexdigest()
    sha256 = hashlib.sha256(inputVal).hexdigest()
    #base64Encode = base64.b64encode(inputVal)
    
    textMD5.configure(state="normal")
    textMD5.delete(1.0,END)
    textMD5.insert(INSERT,md5)
    textMD5.configure(state="disabled")

    textSHA1.configure(state="normal")
    textSHA1.delete(1.0,END)
    textSHA1.insert(INSERT,sha1)
    textSHA1.configure(state="disabled")
    
    textSHA256.configure(state="normal")
    textSHA256.delete(1.0,END)
    textSHA256.insert(INSERT,sha256)
    textSHA256.configure(state="disabled") 
    '''
    textBase64Encode.configure(state="normal")
    textBase64Encode.delete(1.0,END)
    textBase64Encode.insert(INSERT,base64Encode)
    textBase64Encode.configure(height=1+len(base64Encode)/64,state="disabled")
    '''
submit = Button(root, text ="Submit",command = doHash)
inputLabel.pack()
inputEntry.pack()
inputEntry.focus_set()
submit.pack()
md5Label.pack()
textMD5.pack()

sha1Label.pack()
textSHA1.pack()

sha256Label.pack()
textSHA256.pack()
'''
base64EncodeLabel.pack()
textBase64Encode.pack()
'''
root.bind('<Return>',doHash)
root.mainloop()
