
#?===============================Import Libraries=============================
#Todo: import tkinter module
from tkinter import *
from tkinter.scrolledtext import *

#Todo: other necessery modules
import base64

#Todo: import Class
from ClassVignere import *
#?=============================Initialize Window==============================
#Todo: initialized tkinter which means window created
root = Tk()

#Todo: set the width and height of the window
root.geometry('700x400')
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
_mode = IntVar()
#Todo: variable store the result
_result = StringVar()

#?============================Function to encode==============================
def Encode(key, message):
    '''enc = []

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()'''
    p=message.upper()
    k=key.upper()
    cVignere=CVignere(p,k)
    ciphertext = cVignere.MaHoa()
    return ciphertext

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
    if(_mode.get() == 0):
        _result.set(Encode(private_key.get(),_text.get()))
        Textbox.insert(0,"Hay")
    elif(_mode.get() == 1):
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
    _mode.set(0)
    _result.set("")

#?==========================Labels and Buttons================================
Label(root, font= ("Segoe UI",12,'bold'), text='Message: ').place(x= 60,y=60)
Entry(root,font=("Segoe UI",10),textvariable=_text,bg='ghost white').place(x= 280,y=60, 
        height = 22, width = 350)

Label(root, font= ("Segoe UI",12,'bold'), text='Key: ').place(x= 60,y=90)
Entry(root, font=("Segoe UI",10),textvariable=private_key,bg='ghost white').place(x= 280,y=90,
        height = 22, width = 350)

#Label(root, font= ("Segoe UI",12,'bold'), text='Mode(e-encode, d-decode): ').place(x= 60,y=120)
#Entry(root, font=("Segoe UI",10),textvariable=_mode,bg='ghost white').place(x= 280,y=120)
#* Mode: e-encode, d-decode
Label(root, font= ("Segoe UI",12,'bold'), text='Mode: ').place(x= 60,y=120)
Radiobutton(root, font=("Segoe UI",10,'bold'), text="Encode", variable = _mode, value = 0,
            command = (_mode.get())).place(x = 280, y=120)
Radiobutton(root, font=("Segoe UI",10,'bold'), text="Decode", variable = _mode, value = 1,
            command = (_mode.get())).place(x = 380, y=120)

Entry(root,font=("Segoe UI",10,'bold'),textvariable=_result,
            bg='ghost white').place(x= 280, y=150, height = 50, width = 350,)

Button(root,font=("Segoe UI",10,'bold'),text='RESULT',padx= 2,
            bg='LightGray',command=Mode).place(x= 60, y=150)

Button(root, font = ("Segoe UI",10,'bold') ,text ='RESET' ,width =6, 
            command = Reset,bg = 'LimeGreen', padx=2).place(x=280, y = 250)
Button(root, font = ("Segoe UI",10,'bold') ,text= 'EXIT' , width = 6, 
            command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=380, y = 250)

root.mainloop()

