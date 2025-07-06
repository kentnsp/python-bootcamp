student_records = {
    "Juan":70,
    "Maria":98,
    "Joseph":81,
    "Elise":80,
}

code= "Juan"
print(student_records[code])
print('Not existing in Dictionary',student_records.get("Eliza", -1))



for student_name in student_records.keys():
    print(student_name)

if "John" in student_records:
    print("Existing")
else:
    student_records["John"] = 55

print(student_records)


