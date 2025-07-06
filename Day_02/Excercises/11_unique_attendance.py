attendee_names = set()

attendee_count = int(input('Attendee count: '))

for item in range(attendee_count):
    attendee_name = input("Attendee name: ")
    attendee_names.add(attendee_name)

print('Attendees: ',*attendee_names)

attendee_names.discard('ken')
print('Removed Ken: ',*attendee_names)

random_winner = attendee_names.pop()
print('Random Winner: ', random_winner)
