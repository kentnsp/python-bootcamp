correct_username = "admin"
correct_password = "admin"

username_input = input("Enter username: ")
password_input = input("Enter password: ")

if correct_username == username_input and correct_password == password_input:
    print ("Access Granted")
else:
    print("Access Denied")
