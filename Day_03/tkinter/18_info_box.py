import tkinter
from tkinter import messagebox
root = tkinter.Tk()
messagebox.showinfo(
"Information",
"This is an information message."
)

messagebox.showwarning(
"Warning",
"This is a Warning message."
)

messagebox.showerror(
"Error",
"This is an Error message."
)

# yes or no
response = messagebox.askquestion(
"Question",
"Do you want to continue?"
)

messagebox.showinfo(
"Information",
response
)

# true or false
response = messagebox.askokcancel(
"Ask OK/Cancel",
"Do you want to proceed?"
)


root.mainloop()