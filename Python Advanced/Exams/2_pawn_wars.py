letter = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}


def next_pos_white(row, col):
    return row - 1, col


def next_pos_black(row, col):
    return row + 1, col


size = 8

white_pawn_row, white_pawn_col = 0, 0
black_pawn_row, black_pawn_col = 0, 0

matrix = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "w":
            white_pawn_row, white_pawn_col = row, col
        elif row_elements[col] == "b":
            black_pawn_row, black_pawn_col = row, col
    matrix.append(row_elements)

is_captured = False
is_queen = False


while True:
    next_white_row, next_white_col = next_pos_white(white_pawn_row, white_pawn_col)
    white_pawn_row, white_pawn_col = next_white_row, next_white_col

    if abs(white_pawn_col - black_pawn_col) == 1 and white_pawn_row - black_pawn_row == 0:
        is_captured = True
        print(f"Game over! White win, capture on {letter[black_pawn_col]}{size - black_pawn_row}.")
        break

    if white_pawn_row == 0:
        is_queen = True
        print(f"Game over! White pawn is promoted to a queen at {letter[white_pawn_col]}8.")
        break

    next_black_row, next_black_col = next_pos_black(black_pawn_row, black_pawn_col)
    black_pawn_row, black_pawn_col = next_black_row, next_black_col

    if abs(white_pawn_col - black_pawn_col) == 1 and white_pawn_row - black_pawn_row == 0:
        is_captured = True
        print(f"Game over! Black win, capture on {letter[white_pawn_col]}{size - white_pawn_row}.")
        break

    if black_pawn_row == size - 1:
        is_queen = True
        print(f"Game over! Black pawn is promoted to a queen at {letter[black_pawn_col]}1.")
        break









