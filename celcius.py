from tkinter import*
window = Tk()

window.geometry("450x450")
window.config(bg= "#24E2BC")
window.title("celsius to fahrenheit")

def so():
    temp = float(ui.get())
    ar = (temp * 9/5)+ 32
    text1.config(text= str(ar))

title = Label(window,text= "celsius to fahrenheit",font= ("",25,"bold"),bg= "#24E2BC")
title.pack(pady= 10)

frame = Frame(window)
frame.pack(pady= 60)

text = Label(frame,text= "enter temperature in celsius : ",font= ("",16,"bold"),bg= "#24E2BC")
text.grid(row = 0, column = 0)

ui = Entry(frame)
ui.grid(row = 0, column = 1)

text1 = Label(window,text= "",font= ("",16,"bold"),bg= "#24E2BC")
text1.pack()

submit = Button(window,text= "convert",font= ("",24,"bold"),bg= "#CF24E2", command= so)
submit.pack()


window.mainloop()