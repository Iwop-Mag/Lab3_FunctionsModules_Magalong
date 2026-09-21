# main.py

import grades

# Student Identity Configuration

LAST_NAME = 'Magalong'
STUDENT_ID = 'TUPM-26-1134'

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

# Generate student-unique scores
scores = [
    SEED_DIGIT * 10,
    ID_SUM % 100,
    NAME_LENGTH * 7
]

average = grades.compute_average(scores)
grade = grades.assign_grade(average)
remark = grades.generate_remark(grade)

print('=' * 40)
print(f'Student: {LAST_NAME}')
print(f'Student ID: {STUDENT_ID}')
print(f'Generated Scores: {scores}')
print(f'Average: {round(average, 2)}')
print(f'Grade: {grade}')
print(f'Remark: {remark}')
print('=' * 40)