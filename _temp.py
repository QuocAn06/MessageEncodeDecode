
#?===============================Import Libraries=============================
#Todo: import tkinter module
from tkinter import *
from tkinter import ttk

#Todo: other necessery modules
import base64
#Todo: import Class
from ClassVignere import *
from ClassBelasco import *
from ClassTrithemius import *
from ClassCeasar import*
from ClassTransposeTwoLines import *
from ClassDES import *

#?=============================Initialize Window==============================
root = Tk()
root.title('Message Encode App')
root.geometry("800x380")
#Todo: variable saves the encoded or decoded mode 
_mode = IntVar()

#?==============================Create Label=================================
Label(root, font= ("Segoe UI",13), anchor="e", text='Input Type: ', width=11).place(x= 10,y= 50)
Label(root, font= ("Segoe UI",13), anchor="e", text='Message: ', width=11).place(x= 10,y= 90)
Label(root, font= ("Segoe UI",13), anchor="e", text='Key: ', width=11).place(x= 10,y= 160)
Label(root, font= ("Segoe UI",13), anchor="e", text='Encode Type: ', width=11).place(x= 10,y= 200)
Label(root, font= ("Segoe UI",13), anchor="e", text='Mode: ', width=11).place(x= 10,y= 240)
Label(root, font= ("Segoe UI",13), anchor="w", text='Result: ', width=11).place(x= 400,y= 20)

#?==============================Create Combox=================================
list_InputType=('Text','File')
combobox_1 = ttk.Combobox(root, font=("Segoe UI", 13), width=25)
combobox_1['values'] = list_InputType
combobox_1.current(0)
combobox_1.place(x= 125,y= 50)

list_type=('Vignere', 'Belasco', 'Trithemius', 'Ceasar',
           "Transpose Two Lines", 'DES')
combobox_2 = ttk.Combobox(root, font=("Segoe UI", 13), width=25)
combobox_2['values'] = sorted(list_type)
combobox_2.current(0)
combobox_2.place(x= 125,y= 200)

#_combobox.bind("<<ComboboxSelected>>",window_Update)

#?==============================Add RadioButton===============================
Radiobutton(root, font=("Segoe UI",10,'bold'), text="Encode", variable = _mode, value = 0,
            command = (_mode.get())).place(x = 125, y=242)
Radiobutton(root, font=("Segoe UI",10,'bold'), text="Decode", variable = _mode, value = 1,
            command = (_mode.get())).place(x = 225, y=242)


#?==============================Create Text box===============================
myText = Text(root,font= ("Segoe UI",13), width= 27)
myText.place(x= 125, y= 90, height=60)

myKey = Text(root,font= ("Segoe UI",13), width= 27, state='disabled', bg='#a8a7a5')
myKey.place(x= 125, y= 160, height=25)

myResult =  Text(root,font= ("Segoe UI",13), width= 40)
myResult.place(x= 400, y= 50, height=240)

#?===============================Create Menu==================================
my_menu = Menu(root, background='#ff8000', foreground='black', 
                     activebackground='white', activeforeground='black')
root.config(menu= my_menu)

#?==============================Add File Menu=================================
file_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label= "File", menu= file_menu)
file_menu.add_command(label= "New File")
file_menu.add_separator()
file_menu.add_command(label= "Open File...")
file_menu.add_separator()
file_menu.add_command(label= "Save")
file_menu.add_command(label= "Save As")
file_menu.add_separator()
file_menu.add_command(label= "Exit", command= root.quit)

#?==============================Add Edit Menu=================================
edit_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label= "File", menu= edit_menu)
edit_menu.add_command(label= "Cut")
edit_menu.add_command(label= "Copy")
edit_menu.add_command(label= "Paste")
edit_menu.add_separator()
edit_menu.add_command(label= "Undo")
edit_menu.add_command(label= "Redo")

#?==============================Add Button====================================
Button(root,font=("Segoe UI",10,'bold'),text='RESULT',padx= 2, width= 29,
            bg='#47b828',fg="#FFF").place(x= 125, y=300)

#?=====================Add Status Bar To Bottom Of App========================
status_bar = Label(root, text= 'Ready        ', anchor=E)
status_bar.pack(fill= X, side= BOTTOM, ipady= 5)

root.mainloop()