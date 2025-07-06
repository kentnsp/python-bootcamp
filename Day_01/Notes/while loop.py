# stop_program = False
#
# while not stop_program:
#     choice = input("Provide command: ")
#     if choice == "command 1":
#         print("command 1")
#     elif choice == "command 2":
#         print("command 2")
#     elif choice == "command 3":
#         print("command 3")
#     elif choice == "exit":
#         stop_program = True

count = 0
stop_program = False

while not stop_program:
    choice = input("Provide command: ")
    if choice == "add":
        count+=1
        print(count)
    elif choice == "sub":
        count-=1
        print(count)
    elif choice == "double":
        count *= 2
        print(count)
    elif choice == "exit":
        print("Final count: ", count)
        stop_program = True
