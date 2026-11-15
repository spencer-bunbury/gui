from tkinter import*
window = Tk()

window.geometry("450x450")
window.config(bg= "#24E2BC")
window.title("area calculator")

def so():
    cal = int(ui.get())
    cal2 = int(ui2.get())
    answer = cal*cal2
    text1.config(text= str(answer))

title = Label(window,text= "area calculator",font= ("",25,"bold"),bg= "#24E2BC")
title.pack(pady= 10)

frame = Frame(window)
frame.pack(pady= 20)

text = Label(frame,text= "width : ",font= ("",16,"bold"),bg= "#24E2BC")
text.grid(row = 0, column = 0)

ui = Entry(frame)
ui.grid(row = 0, column = 1)

frame2 = Frame(window)
frame2.pack(pady= 10)

text2 = Label(frame2,text= "length : ",font= ("",16,"bold"),bg= "#24E2BC")
text2.grid(row = 0, column = 0)

ui2 = Entry(frame2)
ui2.grid(row = 0, column = 1)

text1 = Label(window,text= "",font= ("",20,"bold"),bg= "#24E2BC")
text1.pack(pady= 20)

submit = Button(window,text= "calculate",font= ("",24,"bold"),bg= "#3A24E2",command= so)
submit.pack(pady=30)


window.mainloop()