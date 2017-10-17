from tkinter import *

#when your code is unreadable but at least its spooky
while True:
    top = Tk()
    top.geometry("400x200")

    B1 = Button(top, text = "Yes")
    B1.place(x = 240,y = 160)
    B2 = Button(top, text="HELL YES!")
    B2.place(x=300, y=160)

    l1 = Label(top,text='Time to get spooky!',font = ("Serif","18"))
    photo = PhotoImage(file="skeltal2.gif")
    l1.pack(side="right")
    Label(image=(photo)).pack(side="left")

    top.mainloop()