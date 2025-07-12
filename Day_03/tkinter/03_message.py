import tkinter
root = tkinter.Tk()
root.title("Sample GUI Application")
root.geometry("800x400")

text = "Sentence 1 Sentence 2 Sentence 3"
message = tkinter.Message(root, text = text)
message.pack()

root.mainloop()