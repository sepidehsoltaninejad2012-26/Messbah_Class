from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from validation import *
from persiantools import *

person_list = []


def save_click():
    try:
        info = {
            "name": name.get(),
            "family": family.get(),
            "age": age.get(),
            "city": city.get(),
            "phone": phone.validator(phone.get()),
        }

        person_list.append(info)
        messagebox.showinfo("saved", "Person saved")
        name.set("")
        family.set("")
        age.set(0)
        city.set("Tehran")
        phone.set("")


    except EXCEPTION as e:
        messagebox.showerror("Save Error", f"Error {e}")

window = Tk()
window.title ("Profile")
window.geometry("450x300")

#name
Label(window, text="Name").place(x=20, y=20)
name = StringVar()
Entry(window, textvariable=name).place(x=105, y=20)

#family
Label(window, text="Family").place(x=20, y=60)
family = StringVar()
Entry(window, textvariable=family).place(x=105, y=60)

#age
Label(window, text="Age").place(x=20, y=100)
age = IntVar()
Entry(window, textvariable=age).place(x=105, y=100)

#city
Label(window, text="City").place(x=20, y=140)
city = StringVar(value="Tehran")
(ttk.Combobox(window, values=["Shiraz", "Tabriz", "Tehran", "Isfahan", "Rasht", "Ahvaz", "Booshehr", "Ardebil", "Arak", "Hamedan"], textvariable=city, state="readonly").
place(x=105, y=140, width = 140))
Entry(window, textvariable=city).place(x=105, y=140)

#phone
Label(window, text="Phone").place(x=20, y=180)
phone = StringVar()
Entry(window, textvariable=phone).place(x=105, y=180)


Button(window, text="Save", command=save_click).place(x=160, y=220, width=90)
window.mainloop()



