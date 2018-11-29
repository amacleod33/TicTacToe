from board_class import Board
def get_nbr(prompt):
    i = 0

    while i == 0:
        number = input(prompt)
        if number in range(0,9):
            i = 1
        else:
            i = 0
    return number

