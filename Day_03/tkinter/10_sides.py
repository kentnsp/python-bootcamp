import tkinter
root = tkinter.Tk()
root.title("Sample GUI Application")
root.geometry("800x400")

left = tkinter.Label(root, text ="Left")
left.pack(side = "left")

right = tkinter.Label(root, text ="right")
right.pack(side = "right")
root.mainloop()