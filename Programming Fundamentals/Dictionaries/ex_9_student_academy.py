number_of_pairs = int(input())
students_dict = {}
for i in range(number_of_pairs):
    name_of_students = input()
    grade = float(input())

    if name_of_students not in students_dict:
        students_dict[name_of_students] = []
        students_dict[name_of_students] = [grade]
    else:
        students_dict[name_of_students].append(grade)

for name, grades in students_dict.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")



