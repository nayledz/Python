def flights(*args):
    my_dict = {}
    key = args[0]

    for arg in range(len(args)):
        if args[arg] == "Finish":
            break
        else:
            command = str(args[arg])

            if command.isdigit():
                my_dict[key] += int(command)
            else:

                if command not in my_dict:
                    my_dict[command] = 0
                key = command

    return my_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
