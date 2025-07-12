import tkinter
root = tkinter.Tk()
root.geometry("800x400")


label = tkinter.Label(
root,
text="Hello",
fg="red",
bg="yellow",
font=("Arial", 14, "bold italic"),
width=100,
height=50
)
label.pack()

label2 = tkinter.Label(
root,
text="World",
padx= 10,
pady= 50
)
label2.pack()
root.mainloop()