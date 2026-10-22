from tkinter import *
from tkinter import messagebox
from persiantools import *
from validation import *


contact_list = []

def save_click():
    try:
        info = {
            "name": name.get(),
            "family": family.get(),
            "age": age_validator(age.get()),
            "phone": phone_validator(plate.get()),
            "title": title().get()
        }

        contact_list.append(person)
        messagebox.showinfo("Saved", "Contact saved")
        name.set("")
        family.set("")
        age.set(0)
        phone.set("")
        title.set("")

    except Exception as e:
        messagebox.showerror("Save Error", f"Error {e}")

window = Tk()
window.title("Profile")
window.geometry("500x300")

#name
Label(window, text="Name").place(x=20, y=20)
name = StringVar()
Entry(window, textvariable=name).place(x=90, y=20)

#family
Label(window, text="Family").place(x=20, y=60)
family = StringVar()
Entry(window, textvariable=family).place(x=90, y=60)

#age
Label(window, text="Age").place(x=20, y=100)
age = IntVar()
Entry(window, textvariable=age).place(x=90, y=100)

#phone
Label(window, text="Phone").place(x=20, y=140)
phone = StringVar()
Entry(window, textvariable=phone).place(x=90, y=140)

#title
Label(window, text="Title").place(x=20, y=180)
title = StringVar()
Entry(window, textvariable=title).place(x=90, y=180)


Button(window, text="Save", command=save_click).place(x=80, y=220, width=250)
window.mainloop()


