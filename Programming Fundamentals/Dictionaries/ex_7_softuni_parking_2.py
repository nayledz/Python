def softuni_parking():
    number_of_commands = int(input())
    registration_dict = {}
    for n in range(number_of_commands):
        command = input().split(" ")

        if "register" in command:
            register_func(command, registration_dict)
        elif "unregister" in command:
            unregister_func(command, registration_dict)

    for username, license_number in registration_dict.items():
        print(f"{username} => {license_number}")


def register_func(command, registration_dict):

    username = command[1]
    license_number = command[2]
    if username not in registration_dict:
        registration_dict[username] = license_number
        print(f"{username} registered {license_number} successfully")
    else:
        print(f"ERROR: already registered with plate number {registration_dict[username]}")


def unregister_func(command, registration_dict):

    username = command[1]
    if username not in registration_dict:
        print(f"ERROR: user {username} not found")
    else:
        registration_dict.pop(username)
        print(f"{username} unregistered successfully")


softuni_parking()