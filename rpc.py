from tkinter import*
import tkinter.font as font
import random

window = Tk()
list1 = ["rock","paper","scissors"]

window.geometry("450x450")
window.config(bg= "#FFFFFF")
window.title("rock paper scissors")

title = Label(window,text= "rock paper scissors",font= ("",24,"bold"),bg= "#fffffa")
title.pack()

winner_label = Label(window,text= "begin",font= ("",16,"bold"),bg= "#ffffff")
winner_label.pack(pady= 30)

frame = Frame(window,bg= "#ffffff")
frame.pack(pady= 0)

#put commands

button1 = Button(frame,text= "rock",font=("",16,"bold"),bg= "#eefe11")
button1.grid(row= 0,column= 0,padx= 25)

button2 = Button(frame,text= "paper",font=("",16,"bold"),bg= "#e619f0")
button2.grid(row= 0,column= 1,padx= 25)

button3 = Button(frame,text= "scissors",font=("",16,"bold"),bg= "#19ffff")
button3.grid(row= 0,column= 2,padx= 25)

#end of commands

frame2 = Frame(window,bg= "#ffffff")
frame2.pack(pady= 20)

text1 = Label(frame2,text= "your input",font=("",16,"bold"))
text1.grid(row= 0,column= 0)

window.mainloop()









