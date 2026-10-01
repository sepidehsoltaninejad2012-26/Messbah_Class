from tkinter import *

Lesson_list = []

def save_click():
    try:
        info = {
            "Title": title.get(),
            "Teacher": teacher.get(),
            "Duration": duration.get(),
            "unit": unit_validator(unit.get())
        }

        student_list.append(info)
        messagebox.showinfo("saved", "User saved")
        title.set("")
        teacher.set("")
        duration.set("")
        unit.set("")

    except EXCEPTION as e:
        messagebox.showerror("Save Error", f"Error {e}")

window = Tk()
window.title("Profile")
window.geometry("400x200")

#title
Label(window, text="Title").place(x=20, y=20)
title = StringVar()
Entry(window, textvariable=title).place(x=90, y=20)

#teacher
Label(window, text="Teacher").place(x=20, y=60)
teacher = StringVar()
Entry(window, textvariable=teacher).place(x=90, y=60)

#duration
Label(window, text="Duration").place(x=20, y=100)
duration = StringVar()
Entry(window, textvariable=duration).place(x=90, y=100)

#unit
Label(window, text="Unit").place(x=20, y=140)
unit = StringVar()
Entry(window, textvariable=unit).place(x=90, y=140)

Button(window, text="Save", command=save_click).place(x=105, y=180, width=120)

window.mainloop()



