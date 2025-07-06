correct_password ="pass"

password_input = input("Please provide password: ")

correct_password_given = correct_password == password_input

#print("Access: ", correct_password_given)

if correct_password_given :
    print("Access Granted")
else:
    print("Access Denied")