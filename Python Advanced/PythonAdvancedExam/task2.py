first_player, second_player = input().split(', ')
size = 6
matrix = []

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

index = 0
first_player_hit = False
second_player_hit = False
while True:
    row, col = tuple(map(int, input().replace('(', '').replace(')', '').split(', ')))
    index += 1
    if index % 2 != 0 and first_player_hit:
        first_player_hit = False
        continue
    if index % 2 == 0 and second_player_hit:
        second_player_hit = False
        continue

    if matrix[row][col] == "E":
        if index % 2 != 0:
            print(f"{first_player} found the Exit and wins the game!")
            break
        else:
            print(f"{second_player} found the Exit and wins the game!")
            break

    elif matrix[row][col] == "T":
        if index % 2 != 0:
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        else:
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break

    elif matrix[row][col] == "W":
        if index % 2 != 0:
            first_player_hit = True
            print(f"{first_player} hits a wall and needs to rest.")
        else:
            second_player_hit = True
            print(f"{second_player} hits a wall and needs to rest.")
