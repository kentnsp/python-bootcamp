string = input("Enter string: ")
special_count = 0
special_char =" !@#$%^&*()"

for item in string:

    if item in special_char:
       special_count += 1

print(special_count)