command = input()

courses = {}

while ":" in command:
    (name, id, course) = command.split(":")

    if course not in courses:
        courses[course] = dict()
    courses[course][id] = name

    command = input()
command = command.replace("_", " ")

for i in courses[command]:
    print(f"{courses[command][i]} - {i}")