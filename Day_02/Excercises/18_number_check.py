user_input=input("Enter a number: ")
print("initial", user_input)
clean_input = user_input.strip().replace(",","")
print("cleaned", clean_input)
is_numeric = clean_input.isnumeric()

if is_numeric:
    clean_input = int(clean_input)
    print(f"Input {clean_input}  + 1: ", clean_input + 1)
else:
    print("Please enter a valid number.")