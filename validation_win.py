from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from persian_tools import national_id, plate, bill
from persiantools import *

user_list = []

def national_id_validator(param):
    pass


def save_click():
    try:
        info = {
            "national_id": national_id_validator(national_id.get()),
            "city": city.validator(city.get()),
            "phone": phone.validator(phone.get()),
            "card_number": card_number.validator(card_number.get()),
            "plate": plate.validator(plate.get()),
            "bill": bill.validator(bill.get()),
            "enquary": enquary.validation(enquary.get())
        }

        user_list.append(info)
        messagebox.showinfo("saved", "User saved")
        national_id.set("")
        city.set("")
        phone.set("")
        card_number.set("")
        plate.set("")
        bill.set("")
        enquiry.set("")

    except EXCEPTION as e:
        messagebox.showerror("Save Error", f"Error {e}")

window = Tk()
window.title ("Profile")
window.geometry("500x340")


#national_id
label = Label(window, text="National ID").place(x=20, y=20)
national_id = StringVar()
Entry(window, textvariable=national_id).place(x=105, y=20)

#city
Label(window, text="City").place(x=20, y=60)
city = StringVar()
ttk.Combobox(window, textvariable=city, values = ["Shiraz", "Tehran", "Isfehan", "Tabriz"],
             state = "readonly").place(x=105, y=60, width=125)

#phone
Label(window, text="Phone").place(x=20, y=100)
phone = StringVar()
Entry(window, textvariable=phone).place(x=105, y=100)

#card_number
Label(window, text="Card Number").place(x=20, y=140)
card_number = StringVar()
Entry(window, textvariable=card_number).place(x=110, y=140)

#plate
Label(window, text="Plate").place(x=20, y=180)
plate = StringVar()
Entry(window, textvariable=plate).place(x=105, y=180)

#bill
Label(window, text="Bill").place(x=20, y=220)
bill = StringVar()
Entry(window, textvariable=bill).place(x=105, y=220)
#enquary
Label(window, text="Enquiry").place(x=20, y=260)
enquary = StringVar()
Entry(window, textvariable=enquary).place(x=105, y=260)

Button(window, text="Save", command=save_click).place(x=160, y=300, width=120)

window.mainloop()



