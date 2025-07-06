student_scores = [98,75,100,86,100,3]

lowest_score = min(student_scores)
print(f'Lowest: {lowest_score}')

highest_score = max(student_scores)
print(f'Highest: {highest_score}')

average_score = sum(student_scores) / len(student_scores)

print(f'Average: {average_score}')

sorted_student_scores = sorted(student_scores, reverse = True)

print(f'Highest to lowset: {sorted_student_scores}')