#print("Hello world")
"""print("Hello again") shortcut = highlight ctrl /"""
#print("I","am","happy", sep = " - ")

#this is how to make comment

message = "Hello {}! Nice to meet you! I am {}"
print(message)

name = input("Enter Name: ")
nickname = input("Enter Nickname: ")


formatted_message = message.format(name, nickname)
print(formatted_message)


message = "Hello {first}! Nice to meet you! I am {second}"
print(message)

name = input("Enter Name: ")
nickname = input("Enter Nickname: ")


formatted_message = message.format(fist = name, second = nickname)
print(formatted_message)