results_dict = {}
submissions = {}
max_points = 0
while True:
    command = input()
    if command == "exam finished":
        break

    command = command.split("-")
    username = command[0]
    language = command[1]

    if language != "banned":
        points = int(command[2])
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1

        if username not in results_dict:
            max_points = points
            results_dict[username] = [language, points]

        else:
            if points >= max_points:
                max_points = points
                results_dict[username] = [language, max_points]

    elif language == "banned":
        if username in results_dict:
            results_dict.pop(username)


print(f"Results:")
for key, value in results_dict.items():
    print(f"{key} | {value[1]}")
print(f"Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")