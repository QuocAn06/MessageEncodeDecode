

#? Sử dụng thư viện tkinter 
from tkinter import *
from ClassVignere import *

window = Tk()

window.title("Welcome to Quoc An app")

cVignere = CVignere("Have a nice day","ABC")

cVignere.MaHoa()
#Todo: tạo một label
lbl = Label(window, text = cVignere.ciphertext)

lbl.grid(column=0, row=0)

#? mainloop() : vòng lập vô tận của window
window.mainloop()
