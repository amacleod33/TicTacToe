class Board:
    SIZE = 9
    BLANK = 'N'
    constant_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    spots_left = constant_board
    def __init__(self):

        board = []
        for i in range(len(self.constant_board)):
            board.append(self.BLANK)


    def nbr_of_unfilled_slots(self):
        s = 0
        for i in Board.constant_board:
            if i is (int):
                s = s + 1
        return s
    def take_spot(self,taken):
        self.spots_left.remove(self.spots_left[taken])
        return
    def choose_spot_at(self,index):
        return self.spots_left[index]
    def display(self):
        s = 0
        for i in range(3):
            for j in range(3):
                print(self.constant_board[s], ' ', end='')
                s = s + 1
            print('')
        return
    def is_available(self,index):
        for i in self.constant_board:
            if index in self.constant_board:
                return True
            else:
                return False
    def setX(self,index):
        if index in self.constant_board:
            self.constant_board[index].remove(index)
            self.constant_board[index].append('X')
        else:
            return None
        return
    def setO(self,index):
        if index in self.constant_board:
            self.constant_board[index].remove(index)
            self.constant_board[index].append('O')
        else:
            return None
        return
    def win(self):
        win = []
        for i in range(3):
            win.append[self.constant_board[i]]
        if win[0] and win[1] and win[2] == 'X':
            return True
        else:
            return False
    def get_winner(self):
        return
    def full(self):
        for i in self.constant_board:
            if i is not (int):
                return True
        else:
            return False
e = Board()

