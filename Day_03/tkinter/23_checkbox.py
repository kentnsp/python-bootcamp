import tkinter
root = tkinter.Tk()

check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
    root,
    text="Enable",
    variable=check_value
)

checkbox.pack()

radio_var = tkinter.StringVar(value="Option A")
radio1 = tkinter.Radiobutton(
    root, text="Option A", variable=radio_var, value="Option A")
radio1.pack()
radio2 = tkinter.Radiobutton(
    root, text="Option B", variable=radio_var, value="Option B")
radio2.pack()


root.mainloop()