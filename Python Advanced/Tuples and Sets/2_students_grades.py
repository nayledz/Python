number_of_students = int(input())

students_dict = {}
for _ in range(number_of_students):
    student, grade = input().split(' ')
    grade = float(grade)
    if student in students_dict:
        students_dict[student].append(grade)
    else:
        students_dict[student] = [grade]

for student, grades in students_dict.items():
    average_grade = sum(grades) / len(grades)
    grades_formatted = ' '.join((f'{grade:.2f}' for grade in grades))
    print(f"{student} -> {grades_formatted} (avg: {average_grade:.2f})")