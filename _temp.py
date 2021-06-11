
#?===============================Import Libraries=============================
#Todo: import tkinter module
from ClassXOR import CXOR
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

#Todo: other necessery modules
import base64
import string
import random

#Todo: import Class
from ClassVignere import *
from ClassBelasco import *
from ClassTrithemius import *
from ClassCeasar import*
from ClassTransposeTwoLines import *
from ClassDES import *


#?=============================Initialize Window==============================
#Todo: initialized tkinter which means window created
root = Tk()

#Todo: set the title of the window
root.title('Start - Message Encode App')

#Todo: set the width and height of the window
root.geometry("800x380")

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
typeInput= StringVar()
#?========================Function to reset window============================
def Reset():
    #Delete previous text
    myText.delete("1.0",END)
    myKey.delete("1.0",END)
    myResult.delete("1.0",END)

    #Update status bars
    root.title('New File - Message Encode App')
    status_bar.config(text= "New        ")
#?========================Create Auto Key Function============================
def autoKey():
    #Delete previous text
    myKey.delete("1.0",END)

    #Auto key
    letters = string.ascii_lowercase
    key = "".join(random.choice(letters) for i in range(8))

    #Add key to textbox
    myKey.insert(END, key)

#?======================Create Save As File Function==========================
def save_as_file():
    text_file= filedialog.asksaveasfilename(defaultextension= ".*",
                                            initialdir= "C:/Users/Admin/Desktop/BT ATHTTT/_project/A Text Edit/",
                                            title= "Save File",
                                            filetypes=(("Text Files","*.txt"),
                                                        ("HTML Files",".html"),
                                                        ("Python Files","*.py"),
                                                        ("All files","*.*")) )

    if text_file:
        #Update Status Bars
        name= text_file
        status_bar.config(text=f'Saved: {name}        ')
        name= name.replace("C:/Users/Admin/Desktop/BT ATHTTT/_project/Output/","")
        root.title(f'{name} - Message Encode App')

        #Save the file
        text_file= open(text_file, 'w')
        text_file.write(myResult.get(1.0, END))

        #Close the file
        text_file.close()

#?========================Function To Encode==================================
def Encode(key, message):
    ciphertext=""
    _type = _class.get()

    if  _type == "Vignere":
        obj = CVignere(message.upper(),key.upper())
        ciphertext = obj.MaHoa()
    elif _type == "Belasco":
        obj = CBelasco(message.upper(),key.upper())
        ciphertext = obj.MaHoa()
    elif _type == "Trithemius":
        obj = CTrithemius(message.upper())
        ciphertext = obj.MaHoa()
    elif _type == "Ceasar":
        obj = CCeasar(message.upper(),3)
        ciphertext = obj.MaHoa()
    elif _type == "Transpose Two Lines":
        obj = CChuyenViHaiDong(message.upper())
        ciphertext = obj.MaHoa()
    elif _type == "XOR":
        obj = CXOR(message.upper())
        ciphertext = obj.MaHoa()
    elif _type =='DES':
        obj = CDes(message,key)
        ciphertext = repr(obj.MaHoa())
        
    return ciphertext

#?========================Function To Decode==================================
def Decode(key, message):
    plaintext=""
    _type = _class.get()

    if _type == "Vignere":
        obj = CVignere(plaintext,key.upper(),message.upper())
        plaintext = obj.GiaiMa()
    elif _type == "Belasco":
        obj = CBelasco(plaintext,key.upper(),message.upper())
        plaintext = obj.GiaiMa()
    elif _type == "Trithemius":
        obj = CTrithemius(plaintext,message.upper())
        plaintext = obj.GiaiMa()
    elif _type == "Ceasar":
        obj = CCeasar(plaintext,3,message.upper()) 
        plaintext = obj.GiaiMa()
    elif _type == "Transpose Two Lines":
        obj = CChuyenViHaiDong(plaintext,message.upper())
        plaintext = obj.GiaiMa()
    elif _type == "XOR":
        obj = CXOR(message.upper())
        plaintext = obj.MaHoa()
    elif _type =='DES':
        obj = CDes(plaintext,key,message)
        plaintext = obj.GiaiMa().decode("utf-8")

    return plaintext

#?============================GET FILE NAME============================
def getFileName():
    myFile.delete("1.0",END)

    #Grab Filename
    text_file= filedialog.askopenfilename(initialdir= "C:/Users/Admin/Desktop/BT ATHTTT/_project/A Text Edit/", 
                                            title= "Open File",
                                            filetypes= (("Text Files","*.txt"), 
                                                        ("HTML Files","*.html"),
                                                        ("Python Files","*.py"),
                                                        ("All files","*.*")) )
    name = text_file
    myFile.insert(END,name)

#?==============Function To Handle Encode/ Decrypt Request===================
def encryptedResults():
    _mess = StringVar()
    _key = myKey.get(1.0,'end-1c')

    if typeInput.get()== 'Text':
        _mess = myText.get(1.0,'end-1c')
    elif typeInput.get()== 'File':
        text_file= myFile.get(1.0,'end-1c')
        
        #Open the file
        text_file=  open(text_file, 'r')
        _mess= text_file.read()
        
        #Close the opened file
        text_file.close()


    if(_mode.get()== 0):
        _text= 'Encrypted:\n    ' + Encode(_key,_mess)
        myResult.delete('1.0',END)
        myResult.insert(END,_text)
    elif(_mode.get() == 1):
        myResult.delete('1.0',END)
        _text= 'Decrypted:\n    ' + Decode(_key,_mess)
        myResult.insert(END,_text)
    else:
        _result.set('Invalid Mode')

#?====================Function To Choose Type Input===========================
def chooseTypeInput(event):
    type= typeInput.get()

    if type== 'File':
        #Destroy current control elements
        messageLabel.place_forget()
        myText.place_forget()

        #create new control elements
        fileLabel.place(x= 10,y= 90)
        myFile.place(x= 125, y= 90, height=25)
        browserButton.place(x= 297, y=120, height=25)
    elif type== 'Text':
        #Destroy current control elements
        fileLabel.place_forget()
        myFile.place_forget()
        browserButton.place_forget()

        #create new control elements
        messageLabel.place(x= 10,y= 90)
        myText.place(x= 125, y= 90, height=60)

#?========================Function To Thoose Type Encode======================
def chooseTypeEncode(event):
    a = _class.get()
    if a in ["Trithemius","Ceasar","Transpose Two Lines",'XOR']:
        myKey.config(state= DISABLED, bg= '#e3e0dc')
        keyButton.config(state=DISABLED)
    else:
        myKey.config(state= NORMAL, bg= '#ffffff')
        keyButton.config(state=NORMAL)

#?==============================Create Label=================================
Label(root, font= ("Segoe UI",13), anchor="e", text='Input Type: ', 
        width=11).place(x= 10,y= 50)

messageLabel= Label(root, font= ("Segoe UI",13), anchor="e", text='Message: ', 
        width=11)
messageLabel.place(x= 10,y= 90)

fileLabel= Label(root, font= ("Segoe UI",13), anchor="e", text='File name: ', 
        width=11)

Label(root, font= ("Segoe UI",13), anchor="e", text='Key: ', 
        width=11).place(x= 10,y= 160)

Label(root, font= ("Segoe UI",13), anchor="e", text='Encode Type: ', 
        width=11).place(x= 10,y= 200)

Label(root, font= ("Segoe UI",13), anchor="e", text='Mode: ', 
        width=11).place(x= 10,y= 240)

Label(root, font= ("Segoe UI",13), anchor="w", text='Result: ', 
        width=11).place(x= 400,y= 20)

#?==============================Create Combox=================================
list_InputType=('Text','File')
combobox_1 = ttk.Combobox(root, font=("Segoe UI", 13), width=25, 
                            textvariable= typeInput)
combobox_1['values'] = list_InputType
combobox_1.current(0)
combobox_1.place(x= 125,y= 50)
combobox_1.bind("<<ComboboxSelected>>",chooseTypeInput)

list_type=('Vignere', 'Belasco', 'Trithemius', 'Ceasar',
           "Transpose Two Lines", 'DES', 'XOR')
combobox_2 = ttk.Combobox(root, font=("Segoe UI", 13), width=25,
                                textvariable=_class)
combobox_2['values'] = sorted(list_type)
combobox_2.current(0)
combobox_2.place(x= 125,y= 200)
combobox_2.bind("<<ComboboxSelected>>",chooseTypeEncode)

#?==============================Add RadioButton===============================
Radiobutton(root, font=("Segoe UI",10,'bold'), text="Encode", 
    variable = _mode, value = 0, command = (_mode.get())).place(x = 125, y=242)
Radiobutton(root, font=("Segoe UI",10,'bold'), text="Decode", 
    variable = _mode, value = 1, command = (_mode.get())).place(x = 225, y=242)


#?==============================Create Text box===============================
myText = Text(root,font= ("Segoe UI",13), width= 27)
myText.place(x= 125, y= 90, height=60)

myFile = Text(root,font= ("Segoe UI",13), width= 27)

myKey = Text(root,font= ("Segoe UI",13), width= 18)
myKey.place(x= 125, y= 160, height=25)

myResult =  Text(root,font= ("Segoe UI",13), width= 42)
myResult.place(x= 400, y= 50, height=240)

#?===============================Create Menu==================================
my_menu = Menu(root, background='#ff8000', foreground='black', 
                     activebackground='white', activeforeground='black')
root.config(menu= my_menu)

#?==============================Add File Menu=================================
file_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label= "File", menu= file_menu)
file_menu.add_command(label= "New", command= Reset, 
                        accelerator='Ctrl+N')
file_menu.add_separator()
file_menu.add_command(label= "Save",accelerator='Ctrl+S')
file_menu.add_command(label= "Save As",command= save_as_file,
                        accelerator='Ctrl+Shift+S')
file_menu.add_separator()
file_menu.add_command(label= "Exit", command= root.quit, accelerator='Ctrl+E')

#?==============================Add Edit Menu=================================
edit_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label= "Edit", menu= edit_menu) 
edit_menu.add_command(label= "Cut")
edit_menu.add_command(label= "Copy")
edit_menu.add_command(label= "Paste")


#?==============================Add Button====================================
resultButton= Button(root,font=("Segoe UI",10,'bold'),text= 'RESULT',padx= 2, 
                width= 29, bg='#47b828',fg="#FFF", command= encryptedResults)
resultButton.place(x= 125, y=300)

browserButton= Button(root,font=("Segoe UI",10,'bold'),text= 'Browser',padx= 2,
                width= 8, bg='#c9c7c5',fg="#000000", command= getFileName)

keyButton= Button(root,font=("Segoe UI",10,'bold'),text= 'Random',padx= 2,
                width= 8, bg='#c9c7c5',fg="#000000", command= autoKey)
keyButton.place(x= 297, y=160, height=25)

#?=====================Add Status Bar To Bottom Of App========================
status_bar = Label(root, text= 'Ready        ', anchor=E)
status_bar.pack(fill= X, side= BOTTOM, ipady= 5)

root.mainloop()