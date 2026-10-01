from tkinter import *
from tkinter import messagebox
from persiantools import *

parking_list = []

def save_click():
    try:
        info = {
            "name": name.get(),
            "color": color.get(),
            "plate": plate_validator(plate.get()),
            "enter_time": enter_time().get(),
        }

        parking_list.append(car)
        messagebox.showinfo("Saved", "Car saved")
        name.set("")
        color.set("")
        plate.set("")
        enter_time.set(00)

    except Exception as e:
        messagebox.showerror("Save Error", f"Error {e}")


window = Tk()
window.title("Profile")
window.geometry("300x220")

# Name
Label(window, text="Name").place(x=20, y=20)
name = StringVar()
Entry(window, textvariable=name).place(x=105, y=20)

#color
Label(window, text="Color").place(x=20, y=60)
color = StringVar()
Entry(window, textvariable=name).place(x=105, y=60)

#plate
Label(window, text="Plate").place(x=20, y=100)
plate = StringVar()
Entry(window, textvariable=plate).place(x=105, y=100)

#enter_time
label = Label(window, text="Enter Time").place(x=20, y=140)
enter_time = StringVar()
entry = Entry(window, textvariable=enter_time).place(x=105, y=140)


Button(window, text="Save", command=save_click).place(x=80, y=180, width=80)

window.mainloop()