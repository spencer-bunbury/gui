from tkinter import*
import calendar

window = Tk()
window.title("calendar")
window.geometry("300x250")
window.config(bg= "#24E2BC")

def sc():
    n_g = Tk()
    n_g.geometry("500x500")
    year_fetch = year_input.get()
    cal_content =calendar.calendar(int(year_fetch))
    label = Label(n_g,text= cal_content)
    label.pack()  

title = Label(window,text= "Calendar",font= ("",16,"bold"),bg= "#24E2BC")
title.pack()

title2 = Label(window,text= "enter year",font= ("arial",12,),bg= "#24E2BC")
title2.pack()

year_input = Entry(window)
year_input.pack(pady= 20)

submit = Button(window,text= "show calender",font= ("arial",16,"bold"),bg= "pink")
submit.pack()


window.mainloop()