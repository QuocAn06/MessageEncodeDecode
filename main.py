#===============================Import Libraries==============================
#Todo: import tkinter module
from tkinter import *

#Todo: other necessery modules
import base64

#=============================Initialize Window===============================
root = Tk()

root.geometry('500x600')
root.resizable(0,0)
root.title("Message Encode and Decode")

Label(root, text='ENCODE DECODE',font= 'arial 16 bold').pack()

Label(root, text ='Đồ án: An Toàn Thông Tin', font = 'arial 13 bold').pack(side =BOTTOM)

#==============================Define variables===============================