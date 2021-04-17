
#?===============================Import Libraries=============================
#Todo: import tkinter module
from tkinter import *

#Todo: other necessery modules
import base64

#?=============================Initialize Window==============================
#Todo: initialized tkinter which means window created
root = Tk()

#Todo: set the width and height of the window
root.geometry('500x600')
#Todo: set the fixed size of the window
root.resizable(0,0)
#Todo: set the title of the window
root.title("Message Encode and Decode")

#Todo: Create Labels that are lines that cannot be changed by the user 
Label(root, text='ENCODE DECODE',font= 'arial 16 bold').pack()
Label(root, text ='Đồ án: An Toàn Thông Tin', font = 'arial 13 bold').pack(side =BOTTOM)

#?==============================Define variables==============================
#Todo: variable that stores the message value 
_text = StringVar()
#Todo:  variable stores the key for encoded and decoded
private_key = StringVar()
#Todo: variable saves the encoded or decoded mode 
_mode = StringVar()
#Todo: variable store the result
_result = StringVar()

#?============================Function to encode==============================
def Encode(key, message):
    enc = []

    for i in range(len(message)):
        key_c = key[i%len(key)]
        enc.append(chr(ord(message[i]) + ord(key_c)) % 256)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#?===========================Function to decode===============================
def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])-ord(key_c)) % 256))
    
    return "".join(dec)

#?=========================Function to set mode===============================
def Mode():
    if(_mode.get() == 'e'):
        _result.set(Encode(private_key.get(),_text.get()))
    elif(_mode.get() == 'd'):
        _result.set(Decode(private_key.get(),_text.get()))
    else:
        _result.set('Invalid Mode')

#?========================Function to exit window=============================
def Exit():
    root.destroy()
#?========================Function to reset window============================
def Reset():
    _text.set("")
    private_key.set("")
    _mode.set("")
    _result.set("")
    
#?==========================Labels and Buttons================================