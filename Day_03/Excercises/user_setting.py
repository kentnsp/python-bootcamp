import tkinter
import json
from tkinter import messagebox

root = tkinter.Tk()
root.title("User Setting")
root.geometry("300x200")

# cell_1_1 = tkinter.Label(root, text="1,1", bg="gray", width=15, height=2)
# cell_1_1.grid(row=1, column=1)

#Name
name_label = tkinter.Label(root, text= "Name:", width=15, height=2)
name_label.grid(row=1, column=1)


name = tkinter.Entry(root)
name.grid(row=1, column=2)


#Age
age_label = tkinter.Label(root, text= "Age:")
age_label.grid(row=2, column=1)

age = tkinter.Entry(root)
age.grid(row=2, column=2)

#Theme
theme_label = tkinter.Label(root, text= "Preferred Theme:")
theme_label.grid(row=3, column=1)

radio_var = tkinter.StringVar(value="Light")
radio1 = tkinter.Radiobutton(
    root, text="Light", variable=radio_var, value="LightA")
radio1.grid(row=3, column=2)

radio2 = tkinter.Radiobutton(
    root, text="Dark", variable=radio_var, value="Dark")
radio2.grid(row=3, column=3)

#Newsletter
check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
    root,
    text="Subscribe to newsletter",
    variable=check_value
)

checkbox.grid(row=4, column=0, columnspan=4)

#Rating
rating_label = tkinter.Label(root, text= "Rate us:")
rating_label.grid(row=5, column=1)

slider_value = tkinter.IntVar(value=0)

slider = tkinter.Scale(
    root,
    from_=0,
    to=5,
    orient="horizontal",
    variable=slider_value
    )

slider.grid(row=5, column=2)


def submit():
    given_name = name.get()
    given_age = age.get()
    given_theme = radio_var.get()
    given_newsletter = check_value.get()
    given_rating = slider_value.get()


    user = [
        { 'Name': given_name,
          'Age': given_age,
          'Theme': given_theme,
          'Subscribe' : given_newsletter,
          'Rating' : given_rating
        }
    ]

    with open('user.json', 'w') as file:
        json.dump(user, file, indent=4)






button = tkinter.Button(root, text="Submit", command=submit)
button.grid(row=7, column=0, columnspan=4)


root.mainloop()
