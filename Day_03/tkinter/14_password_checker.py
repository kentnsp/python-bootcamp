import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("Password Checker")
root.geometry("300x100")

header = tkinter.Label(root, text= "Enter your password:")
header.pack()

entry = tkinter.Entry(root, show="*")
entry.pack()

user_input = tkinter.StringVar(root, value="Enter your password and Submit")
label = tkinter.Label(root, textvariable= user_input)
label.pack()

def show_input():
    given_pass = entry.get()

    if given_pass == "pass":
        message = "Password correct! Access granted."
    else:
        messagebox.showerror(
            "Error",
            "Incorrect password"
        )
        message = "Incorrect password. Try again"

    user_input.set(message)

button = tkinter.Button(root, text="Submit", command=show_input)
button.pack()

root.mainloop()
