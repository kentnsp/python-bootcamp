# attendees = ["Mia Anderson",
#              "Ethan Roberts",
#              "Liam Johnson",
#              "Sophia Martinez",
#              "Olivia Davis",
#              "Noah Thompson"]
#
# with open("test.txt", "w") as file:
#
#         for attendee in attendees:
#          file.write(attendee)
#          file.write('\n')

# def writelogs(message):
#    with open("test.txt", "a") as file:
#         file.write(message)
#         file.write("\n")
#
#
# writelogs("Alex Freze")
# writelogs("Ken Lico")

with open("test.txt", "r") as file:
    file_contents = file.read().splitlines()
    print(file_contents)


