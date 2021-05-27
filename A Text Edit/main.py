from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('MyCode - My TextPad!')
root.iconbitmap("C:/Users/Admin/Desktop/BT ATHTTT/_project/A Text Edit/image/alienware.ico")
root.geometry("1000x676")

#Create New File Function
def new_file():
    #Delete previous text
    my_text.delete("1.0",END)

    #Update status bars
    root.title('New File - My TextPad!')
    status_bar.config(text= "New File        ")

#Create Open file Function
def open_file():
    #Delete previous text
    my_text.delete("1.0",END)

    #Grab Filename
    text_file= filedialog.askopenfilename(initialdir= "C:/Users/Admin/Desktop/BT ATHTTT/_project/A Text Edit/", 
                                          title= "Open File",
                                          filetypes= (("Text Files","*.txt"), 
                                                      ("HTML Files","*.html"),
                                                      ("Python Files","*.py"),
                                                      ("All files","*.*")) )
    
    #Update status bars
    name = text_file
    status_bar.config(text=f'{name}        ')
    name= name.replace("C:/Users/Admin/Desktop/BT ATHTTT/_project/A Text Edit/","")
    root.title(f'{name} - TextPad!')

    #Open the file
    text_file=  open(text_file, 'r')
    stuff= text_file.read()
    #Add file to textbox
    my_text.insert(END, stuff)
    #Close the opened file
    text_file.close()

#Create Save As File Function
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
        status_bar.config(text=f'{name}        ')
        name= name.replace("C:/Users/Admin/Desktop/BT ATHTTT/_project/A Text Edit/","")
        root.title(f'{name} - TextPad!')

        #Save the file
        text_file= open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        #Close the file
        text_file.close()

#Create main Frame
my_frame= Frame(root)
my_frame.pack(pady=5)

#Create our Scrollbar For the Text Box
text_scroll= Scrollbar(my_frame)
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
file_menu.add_command(label= "New File", command= new_file)
file_menu.add_separator()
file_menu.add_command(label= "Open File...", command= open_file)
file_menu.add_separator()
file_menu.add_command(label= "Save")
file_menu.add_command(label= "Save As", command= save_as_file)
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
status_bar = Label(root, text= 'Ready        ', anchor=E)
status_bar.pack(fill= X, side= BOTTOM, ipady= 5)





root.mainloop()