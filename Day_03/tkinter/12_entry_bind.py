import tkinter
root = tkinter.Tk()
root.geometry("500x400")

entry = tkinter.Entry(root)
entry.pack()

def show_input(event):
    #    print("Enter pressed")

#print in console
    # user_input = entry.get()
    # print(user_input)

#print in form
    text = tkinter.StringVar(root, value="Hello")
    label = tkinter.Label(root, textvariable=text)

    given_text = entry.get()
    label = tkinter.Label(root, text=given_text)
    label.pack()

root.bind("<Return>", show_input)
root.bind("<space>", show_input)
root.mainloop()
