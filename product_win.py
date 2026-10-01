from tkinter import *

product_list = []

def save_click():
    try:
        info = {
            "name": name.get(),
            "quantity": quantity.get(),
            "price": price.get(),
            "description": description.get(),
            "total_price": total_price.get()
        }

        product_list.append(info)
        messagebox.showinfo("saved", "Product saved")
        name.set("")
        quantity.set("")
        price.set("")
        description.set("")
        total_price.set("")

    except EXCEPTION as e:
        messagebox.showerror("Save Error", f"Error {e}")

window = Tk()
window.title("Profile")
window.geometry("400x250")

#name
Label(window, text="Name").place(x=20, y=20)
name= StringVar()
Entry(window, textvariable=name).place(x=90, y=20)

#quantity
Label(window, text="Quantity").place(x=20, y=60)
quantity = StringVar()
Entry(window, textvariable=quantity).place(x=90, y=60)

#price
Label(window, text="Price").place(x=20, y=100)
price = StringVar()
Entry(window, textvariable=price).place(x=90, y=100)

#description
Label(window, text="Description").place(x=20, y=140)
description = StringVar()
Entry(window, textvariable=description).place(x=90, y=140)

#total_price
Label(window, text="Total_price").place(x=20, y=180)
total_price = StringVar()
Entry(window, textvariable=total_price).place(x=90, y=180)



Button(window, text="Save", command=save_click).place(x=105, y=220, width=120)

window.mainloop()