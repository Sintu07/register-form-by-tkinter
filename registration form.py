from tkinter import *
from PIL import Image, ImageTk


win = Tk()
win.geometry("800x600")
img = Image.open("S:/image/back.jpg")
img = img.resize((800, 600))
img_tk = ImageTk.PhotoImage(img, master=win)
l = Label(win, image=img_tk)
l.place(x=0, y=0)


# frame***********************************

# frame 1 ***********************************************************************************
frm1 = Frame(win, bg="light yellow", bd=12)
frm1.place(x=300, y=100, width=500, height=400)

frm2 = Frame(win, bg="light blue", bd=12)
frm2.place(x=0, y=100, width=300, height=400)


def sub():
    first = e1.get()
    last = e2.get()
    contact = e3.get()
    email = e4.get()
    password = e5.get()
    cpassword = e6.get()


# LAbeel


Label(frm1, text="Registration Form", font=("", 22, "bold"),
      bd=8, background="light yellow").grid(row=0, column=0)


first = Label(frm1, text="First Name", width=12, bd=8, font=(
    "", 22, "bold"), background="white").grid(row=1, column=0)
last = Label(frm1, text="Last  Name", width=12, bd=8, font=(
    "", 22, "bold"), background="white").grid(row=2, column=0)
contact = Label(frm1, text="Contact No.", width=12, bd=8, font=(
    "", 20, "bold"), background="white").grid(row=3, column=0)
email = Label(frm1, text="Emai", width=12, bd=8, font=(
    "", 22, "bold"), background="white").grid(row=4, column=0)
pswd = Label(frm1, text="password", width=12, bd=8, font=(
    "", 22, "bold"), background="white").grid(row=5, column=0)
cpaswd = Label(frm1, text="Confirm password", width=16, bd=8, font=(
    "", 18, "bold"), background="white").grid(row=6, column=0)


# enetry


e1 = Entry(frm1, width=22, bd=8, background="white")
e1.grid(row=1, column=1)
e2 = Entry(frm1, width=22, bd=8, background="white")
e2.grid(row=2, column=1)
e3 = Entry(frm1, width=22, bd=8, background="white")
e3.grid(row=3, column=1)
e4 = Entry(frm1, width=22, bd=8, background="white")
e4.grid(row=4, column=1)
e5 = Entry(frm1, width=22, bd=8, background="white")
e5.grid(row=5, column=1)
e6 = Entry(frm1, width=22, bd=8, background="white")
e6.grid(row=6, column=1)


# buttom******************************************************
b1 = Button(win, text="submit", width=18, command=sub)
b1.place(x=350, y=520)

win.mainloop()
