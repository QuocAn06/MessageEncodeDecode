from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('My TextPad!')
root.iconbitmap("c:/Users/Admin/Desktop/BT ATHTTT/_project/A Text Edit/image/alienware.ico")
root.geometry("1000x660")

#Create main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#Create our Scrollbar For the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Create Text Box
my_text = Text(my_frame, width= 88, height= 25, font=("Segoe UI", 16), 
               selectbackground="blue", selectforeground="white", undo= True,
               yscrollcommand=text_scroll.set)
my_text.pack()

#Configure our Scrollbar
text_scroll.config(command= my_text.yview)

root.mainloop()