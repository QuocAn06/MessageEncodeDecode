from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('My TextPad!')
root.iconbitmap("c:/Users/Admin/Desktop/BT ATHTTT/_project/A Text Edit/image/alienware.ico")
root.geometry("1000x676")

#Create main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#Create our Scrollbar For the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Create Text Box
my_text = Text(my_frame, width= 97, height= 25, font=("Segoe UI", 14), 
               selectbackground="#0099FF", selectforeground="#FFFFFF", undo= True,
               yscrollcommand=text_scroll.set)
my_text.pack()

#Configure our Scrollbar
text_scroll.config(command= my_text.yview)

#Create Menu
my_menu = Menu(root)
root.config(menu= my_menu)

#Add File Menu
file_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label= "File", menu= file_menu)
file_menu.add_command(label= "New File")
file_menu.add_separator()
file_menu.add_command(label= "Open File...")
file_menu.add_separator()
file_menu.add_command(label= "Save")
file_menu.add_separator()
file_menu.add_command(label= "Exit", command= root.quit)

#Add Edit Menu
edit_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label= "File", menu= edit_menu)
edit_menu.add_command(label= "Cut")
edit_menu.add_command(label= "Copy")
edit_menu.add_command(label= "Paste")
edit_menu.add_separator()
edit_menu.add_command(label= "Undo")
edit_menu.add_command(label= "Redo")

#Add Status Bar  To Bottom Of Add
status_bar = Label(root, text= 'Ready    ', anchor=E)
status_bar.pack(fill= X, side= BOTTOM, ipady= 5)





root.mainloop()