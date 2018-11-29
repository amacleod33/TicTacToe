class Board:
    SIZE = 9
    BLANK = 'N'
#initialize constand board, spots left, and board
    def __init__(self):
        self.constant_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.spots_left = self.constant_board
        self.board = ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
#function returns the number of spots left
    def nbr_of_unfilled_slots(self):
        s = 0
        for i in self.spots_left:
            if i in range(0,10):
                s = s + 1
        return s

#function takes removes taken from spots_left list
    def take_spot(self, taken):
        return self.spots_left.remove(taken)

#function returns index of spots_left
    def choose_spot_at(self, index):
        return self.spots_left[index]

#creates a display of the tic tac toe board
    def display(self):
        s = 0
        for i in range(3):
            for j in range(3):
                print(self.board[s], ' ', end='')
                s = s + 1
            print('')
        return

#returns true or false depending on if the index is in spots_left
    def is_available(self, index):
        for i in self.spots_left:
            if index in self.spots_left:
                return True
            else:
                return False

#puts x in indicated index in board and removed index from spots_left
    def setX(self, index):
        if index in self.spots_left:
            self.board.remove(self.board[index-1])
            self.board.insert(index-1, 'X')
            self.spots_left.remove(index)
        else:
            return None
        return

#puts o in indicated index in board and removes index from spots_left
    def setO(self, index):
        if index in self.spots_left:
            self.board.remove(self.board[index-1])
            self.board.insert(index-1, 'O')
            self.spots_left.remove(index)
        else:
            return None
        return

#determines if there is a winner
    def win(self):
        if self.board[0] == 'O' and self.board[1] == 'O' and self.board[2] == 'O' or self.board[0] == 'X' and self.board[1] == 'X' and self.board[2] == 'X':
            return True
        elif self.board[0] == 'X' and self.board[3] == 'X' and self.board[6] == 'X' or self.board[0] == 'O' and self.board[3] == 'O' and self.board[6] == 'O':
            return True
        elif self.board[1] == 'X' and self.board[4] == 'X' and self.board[7] == 'X' or self.board[1] == 'O' and self.board[4] == 'O' and self.board[7] == 'O':
            return True
        elif self.board[2] == 'X' and self.board[5] == 'X' and self.board[8] == 'X' or self.board[2] == 'O' and self.board[5] == 'O' and self.board[8] == 'O':
            return True
        elif self.board[3] == 'X' and self.board[4] == 'X' and self.board[5] == 'X' or self.board[3] == 'O' and self.board[4] == 'O' and self.board[5] == 'O':
            return True
        elif self.board[6] == 'X' and self.board[7] == 'X' and self.board[8] == 'X' or self.board[6] == 'O' and self.board[7] == 'O' and self.board[8] == 'O':
            return True
        elif self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X' or self.board[0] == 'O' and self.board[4] == 'O' and self.board[8] == 'O':
            return True
        elif self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X' or self.board[2] == 'O' and self.board[4] and self.board[6] == 'O':
            return True
        else:
            return False

#returns the winning letter
    def get_winner(self):
        if self.board[0] == 'X' and self.board[1] == 'X' and self.board[2] == 'X':
            return 'X'
        elif self.board[0] == 'O' and self.board[1] == 'O' and self.board[2] == 'O':
            return 'O'
        elif self.board[0] == 'X' and self.board[3] == 'X' and self.board[6] == 'X':
            return 'X'
        elif self.board[0] == 'O' and self.board[3] == 'O' and self.board[6] == 'O':
            return 'O'
        elif self.board[1] == 'X' and self.board[4] == 'X' and self.board[7] == 'X':
            return 'X'
        elif self.board[1] == 'O' and self.board[4] == 'O' and self.board[7] == 'O':
            return 'O'
        elif self.board[2] == 'X' and self.board[5] == 'X' and self.board[8] == 'X':
            return 'X'
        elif self.board[2] == 'O' and self.board[5] == 'O' and self.board[8] == 'O':
            return 'O'
        elif self.board[3] == 'X' and self.board[4] == 'X' and self.board[5] == 'X':
            return 'X'
        elif self.board[3] == 'O' and self.board[4] == 'O' and self.board[5] == 'O':
            return 'O'
        elif self.board[6] == 'X' and self.board[7] == 'X' and self.board[8] == 'X':
            return 'X'
        elif self.board[6] == 'O' and self.board[7] == 'O' and self.board[8] == 'O':
            return 'O'
        elif self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X':
            return 'X'
        elif self.board[0] == 'O' and self.board[4] == 'O' and self.board[8] == 'O':
            return 'O'
        elif self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X':
            return 'X'
        elif self.board[2] == 'O' and self.board[4] == 'O' and self.board[6] == 'O':
            return 'O'
        else:
            return 'N'

#determines if the board is full
    def full(self):
        if len(self.spots_left) == 0:
            return True
        else:
            return False


