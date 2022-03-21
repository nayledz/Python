courses_dict = {}

while True:
    command = input()
    if command == "end":
        break
    command = command.split(' : ')
    course = command[0]
    name_of_student = command[1]
    if course not in courses_dict:
        courses_dict[course] = []
        courses_dict[course] = [name_of_student]
    else:
        courses_dict[course].append(name_of_student)

for course, value in courses_dict.items():
    print(f"{course}: {len(value)}")
    for i in value:
        print(f"-- {i}")
