command = input()

telephone_numbers = {}

while True:
    if command.isdigit():
        number = int(command)
        for i in range(number):
            name = input()
            if name not in telephone_numbers:
                print(f"Contact {name} does not exist.")
            else:
                print(f"{name} -> {telephone_numbers[name]}")
        break
    data = command.split("-")
    person_name = data[0]
    telephone = data[1]
    if person_name not in telephone_numbers:
        telephone_numbers[person_name] = 0
    telephone_numbers[person_name] = telephone

    command = input()