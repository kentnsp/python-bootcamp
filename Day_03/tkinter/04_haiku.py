import tkinter
root = tkinter.Tk()
root.title("Python Haiku")
root.geometry("300x100")

message ="""
Loops within loops spin,
A silent function returns,
The logic is clear.
"""

label = tkinter.Label(root, text = message)
label.pack()

root.mainloop()