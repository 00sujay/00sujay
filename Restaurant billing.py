from tkinter import *
from tkinter import messagebox

log=Tk()
log.title("LOGIN")
log.geometry("925x500")

def sign_in():
    u=username.get()
    p=passw.get()

    if u=='admin' and p=='admin':
        window=Toplevel(log)
        window.title("Billing")
        window.geometry("1200x1080")

        def billing():
            cost = {"Chicken Fried Rice": [e1, 150], "Veg Fried Rice": [e2, 120],
                    "Chilly Chicken": [e3, 140], "Egg Fried Rice": [e4, 120],
                    "Chicken Manchurian": [e5, 160], "Egg Chilly": [e6, 120]}
            total = 0

            for key, value in cost.items():
                if value[0].get() != "":
                    total += int(value[0].get()) * value[1]
                    label17 = Label(window, text=total, font="times 20")
                    label17.place(x=450, y=580)

        window.configure(bg="#a7b6c7")

        label1 = Label(window, text="FAST FOOD",fg="#242433",bg="#a7b6c7",font="sans 35 bold")
        label1.place(x=400, y=20)

        label2 = Label(window, text="MENU",fg="#b53f3f",bg="#a7b6c7",font="sans 35 bold")
        label2.place(x=900, y=130)

        label3 = Label(window, text="Chicken Fried Rice   Rs150",fg="#2c0d5c",bg="#a7b6c7", font="times 30 italic")
        label3.place(x=800, y=200)

        label4 = Label(window, text="Veg Fried Rice          Rs120",fg="#2c0d5c",bg="#a7b6c7", font="times 30 italic")
        label4.place(x=800, y=270)

        label5 = Label(window, text="Chilly Chicken           Rs140",fg="#2c0d5c",bg="#a7b6c7", font="times 30 italic")
        label5.place(x=800, y=340)

        label6 = Label(window, text="Egg Fried Rice            Rs120",fg="#2c0d5c",bg="#a7b6c7", font="times 30 italic")
        label6.place(x=800, y=410)

        label7 = Label(window, text="Chicken Manchurian   Rs160",fg="#2c0d5c",bg="#a7b6c7", font="times 30 italic")
        label7.place(x=800, y=480)

        label7 = Label(window, text="Egg Chilly                    Rs120",fg="#2c0d5c",bg="#a7b6c7", font="times 30 italic")
        label7.place(x=800, y=550)

        label9 = Label(window, text="Chicken Fried Rice",fg="#5c1028",bg="#a7b6c7", font="times 18")
        label9.place(x=50, y=200)

        e1 = Entry(window)
        e1.place(x=50, y=240)

        label10 = Label(window, text="Veg Fried Rice",fg="#5c1028",bg="#a7b6c7", font="times 18")
        label10.place(x=50, y=300)

        e2 = Entry(window)
        e2.place(x=50, y=340)

        label11 = Label(window, text="Chilly Chicken",fg="#5c1028",bg="#a7b6c7", font="times 18")
        label11.place(x=50, y=400)

        e3 = Entry(window)
        e3.place(x=50, y=440)

        label12 = Label(window, text="Egg Fried Rice",fg="#5c1028",bg="#a7b6c7", font="times 18")
        label12.place(x=350, y=200)

        e4 = Entry(window)
        e4.place(x=350, y=240)

        label13 = Label(window, text="Chicken Manchurian",fg="#5c1028",bg="#a7b6c7", font="times 18")
        label13.place(x=350, y=300)

        e5 = Entry(window)
        e5.place(x=350, y=340)

        label14 = Label(window, text="Egg Chilly",fg="#5c1028",bg="#a7b6c7", font="times 18")
        label14.place(x=350, y=400)

        e6 = Entry(window)
        e6.place(x=350, y=440)

        b1 = Button(window, text="TOTAL", width=30, command=billing)
        b1.place(x=450, y=540)

        window.mainloop()

        log.mainloop()

    elif u!='admin' and p!='admin':
        messagebox.showerror("Invalid","Invalid credentials")
    elif p!='admin':
        messagebox.showerror("Invalid","Incorrect Password")
    elif u!='admin':
        messagebox.showerror("Invalid","Incorrect username")


img=PhotoImage(file='login.png')
Label(log,image=img,bg='grey').place(x=50,y=50)

frame=Frame(log,width=350,height=350,bg='white')
frame.place(x=480,y=70)

title=Label(frame,text="Sign in",fg='#8f5d85',bg='white',font="calibri 19 bold")
title.place(x=130,y=5)

def enter(e):
    username.delete(0,'end')

def leave(e):
    if username.get()=='':
        username.insert(0,"Enter Username")

username=Entry(frame,width=30,border=0,fg="black",bg="white",font="times 11 italic")
username.place(x=30,y=80)
username.insert(0,'Enter Username')
username.bind('<FocusIn>',enter)
username.bind('<FocusOut>',leave)

Frame(frame,width=350,height=2,bg="black").place(x=30,y=100)

def while_in(e):
    passw.delete(0,'end')

def while_out(e):
    if passw.get()=='':
        passw.insert(0,'Enter Password')

passw=Entry(frame,width=30,border=0,fg="black",bg="white",font="times 11 italic")
passw.place(x=30,y=160)
passw.insert(0,'Enter Password')
passw.bind('<FocusIn>',while_in)
passw.bind('<FocusOut>',while_out)
Frame(frame,width=350,height=2,bg="black").place(x=30,y=180)

Button(frame,width=35,text=("SIGN IN"),padx=15,pady=15,bg="#d0e7f2",fg="black",command=sign_in).place(x=35,y=200)

log.mainloop()