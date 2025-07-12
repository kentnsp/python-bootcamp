import tkinter
root = tkinter.Tk()
root.title("Sample GUI Application")
root.geometry("800x400")

tkinter.Label(root, text="Header").pack()

label = tkinter.Label(root, text="Hello")
label.pack()

next_label = tkinter.Label(root, text="World")
next_label.pack()

message ="""
This is multiple line
This is multiple line 2
"""

label2 = tkinter.Label(root, text = message)
label2.pack()

root.mainloop()
