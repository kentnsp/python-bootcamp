from Day_01.Notes.input import user_input

number = 123456.128456789
print("initial: ",number)
print(f"Sample formating: {number:.2f}")
print(f"Sample comma: {number:,}")
print(f"Sample both: {number:,.2f}")
print(f"Sample %: {number:.2%}")
print()

string = "Hello World"
lower_string = string.lower()
upper_string = string.upper()
title_string = string.title()
print(string)
print(lower_string)
print(upper_string)
print(title_string)
replace_string = title_string.replace(" ", "-")
print(replace_string)



string2 ="    hello world"
all_lower=string2.islower()
print(all_lower)

clean_input = string2.lower().strip()

print("Clean",clean_input)

email_input = input("Enter GMAIL: ")
email = email_input.endswith("@gmail.com")
print(email)


user_input2= input("Enter name and nickname: ")
user_inputs = user_input2.split()

print("SPLIT", user_inputs)

combined = "-".join(user_inputs)
print("JOIN",combined)