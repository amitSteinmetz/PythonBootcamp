from tkinter import *


def button_clicked():
    miles = int(user_input.get())
    km = int(miles * 1.6)
    label_3.config(text=km)


# Window
window = Tk()
window.title("Mile to Km converter")
window.minsize(width=200, height=200)

# Entry
user_input = Entry()
user_input.grid(column=1, row=0)

# Label_1
label_1 = Label(text="Miles", font=("Arial", 10, "normal"))
label_1.grid(column=2, row=0)

# Label_2
label_2 = Label(text="is equal to", font=("Arial", 10, "normal"))
label_2.grid(column=0, row=1)

# Label_3
label_3 = Label(text="0", font=("Arial",  10, "normal"))
label_3.grid(column=1, row=1)

# Label_4
label_4 = Label(text="km", font=("Arial", 10, "normal"))
label_4.grid(column=2, row=1)

# Button
my_button = Button(text="calculate", command=button_clicked)
my_button.grid(column=1, row=2)

mainloop()
