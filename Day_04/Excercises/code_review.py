def attendee(count: int)-> list[str]:
    """
    Function to input number of attendees and their names
    :param count: (int) number of attendees
    :return: (list) string of attendee names
    """
    attendance_names: list[str] = []
    for item in range(count):
         attendee_name = input('Attendee name: ')
         attendance_names.append(attendee_name)
    return attendance_names

attendee_count = int(input('Attendee count: '))
print(attendee(attendee_count))




# print('Index num of "ken": ', attendance_names.index('ken'))
#
# print('Name "ken" count: ', attendance_names.count('ken'))
#
# name_to_rem = 'ken'
# if name_to_rem in attendance_names:
#     attendance_names.remove(name_to_rem)
#     print('Removed "ken": ', attendance_names)
# else:
#     print('"ken" Non existing')
#
# removed_item = attendance_names.pop(-1)
# print('(POP)Late attendee to remove: ', removed_item)
# print('List without late attendee: ', attendance_names)
