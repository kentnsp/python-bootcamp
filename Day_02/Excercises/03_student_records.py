student_names = ("Juan","Maria","Joseph")
student_records = (70, 90, 81)

for index, (name, record) in enumerate(zip(student_names, student_records), start =1):
    print(f"Student {index}: {name} scored {record} in the exam")

    highest_score = record
    highest_name = name

    if record > highest_score:
        highest_score = record
        highest_name = name
        highest_index = index

print(f"Student {highest_index}: {highest_name} scored {highest_score} HIGHEST")