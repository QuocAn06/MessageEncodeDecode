
#?===============================Import Libraries=============================
#Todo: import tkinter module
from tkinter import *
from tkinter.scrolledtext import *
from tkinter import ttk

#Todo: other necessery modules
import base64

#Todo: import Class
from ClassVignere import *
from ClassBelasco import *
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
#Todo: get name class
_class = StringVar()
#?============================Function to encode==============================
def Encode(key, message):
    ciphertext=""
    _type = _class.get()

    if  _type == "Vignere":
        obj=CVignere(message,key)
        ciphertext = obj.MaHoa()
    elif _type == "Belasco":
        obj=CBelasco(message,key)
        ciphertext = obj.MaHoa()
    return ciphertext

#?===========================Function to decode===============================
def Decode(key, message):
    '''dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])-ord(key_c)) % 256))'''
    cVignere = CVignere(" ",key,message)
    plaintext = cVignere.GiaiMa()
    return plaintext

#?=========================Function to set mode===============================
def Mode():
    _mess = (_text.get()).upper()
    _key = (private_key.get()).upper()

    if(_mode.get() == 0):
        _result.set(Encode(_key,_mess))
    elif(_mode.get() == 1):
        _result.set(Decode(_key,_mess))
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
Entry(root,font=("Segoe UI",10),textvariable=_text, bg='ghost white').place(x= 280,y=60, 
        height = 22, width = 350)

Label(root, font= ("Segoe UI",12,'bold'), text='Key: ').place(x= 60,y=90)
Entry(root, font=("Segoe UI",10),textvariable=private_key, bg='ghost white').place(x= 280,y=90,height = 22, width = 350)

#* Type encoding
Label(root, font= ("Segoe UI",12,'bold'), text='Encoding type: ').place(x= 60,y=120)
_combobox = ttk.Combobox(root,font=("Segoe UI",10,'bold'),
                textvariable=_class)
_combobox['values'] = ('Vignere','Belasco')
_combobox.current(1)
_combobox.place(x=280,y=120)

#* Mode: e-encode, d-decode
Label(root, font= ("Segoe UI",12,'bold'), text='Mode: ').place(x= 60,y=150)
Radiobutton(root, font=("Segoe UI",10,'bold'), text="Encode", variable = _mode, value = 0,
            command = (_mode.get())).place(x = 280, y=150)
Radiobutton(root, font=("Segoe UI",10,'bold'), text="Decode", variable = _mode, value = 1,
            command = (_mode.get())).place(x = 380, y=150)

Entry(root,font=("Segoe UI",10,'bold'),textvariable=_result,
            bg='ghost white').place(x= 280, y=180, height = 50, width = 350,)

Button(root,font=("Segoe UI",10,'bold'),text='RESULT',padx= 2,
            bg='LightGray',command=Mode).place(x= 60, y=180)

Button(root, font = ("Segoe UI",10,'bold') ,text ='RESET' ,width =6, 
            command = Reset,bg = 'LimeGreen', padx=2).place(x=280, y = 280)
Button(root, font = ("Segoe UI",10,'bold') ,text= 'EXIT' , width = 6, 
            command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=380, y = 280)

root.mainloop()

