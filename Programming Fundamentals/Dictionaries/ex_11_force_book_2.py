command = input()

force_book_dict = {}
while True:
    if command == "Lumpawaroo":
        break

    elif "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]

        condition = [current_side for current_side in force_book_dict if force_user in force_book_dict[current_side]]
        if len(condition) == 0:
            condition.clear()

            if force_side not in force_book_dict:
                force_book_dict[force_side] = [force_user]
            else:
                force_book_dict[force_side].append(force_user)

    elif "->" in command:
        command = command.split(" -> ")
        force_user = command[0]
        force_side = command[1]
        for current_side in force_book_dict:
            if force_user in force_book_dict[current_side]:
                if len(force_book_dict[current_side]) > 1:
                    force_book_dict[current_side].pop(force_user)
                    break
                else:
                    del force_book_dict[current_side]
                    break

        if force_side in force_book_dict:
            force_book_dict[force_side].append(force_user)
        else:
            force_book_dict[force_side] = [force_user]

        print(f"{force_user} joins the {force_side} side!")

    command = input()

for data in force_book_dict:
    print(f'Side: {data}, Members: {len(force_book_dict[data])}')
    for name in force_book_dict[data]:
        print(f'! {name}')