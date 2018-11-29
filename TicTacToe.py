import random
from board_class import Board
from get_nbr import get_nbr


class TicTacToe:
    def __init__(self):
        self.board = Board()
    def get_player_char(self):
        x_or_o = input('Would you like to be X or O')
        while x_or_o is not 'x' and x_or_o is not 'X' and x_or_o is not 'o' and x_or_o is not 'O':
            x_or_o = input('Please enter an x or o')
        if x_or_o is 'x':
            x_or_o = 'X'
        elif x_or_o is 'o':
            x_or_o = 'O'
        return x_or_o

    def get_player_spot(self):

        i = 0
        while i < 1:
            number = int(input('Enter a number for your x or o'))
            if number == 1 or number == 2 or number == 3 or number == 4 or number == 5 or number == 6 or number == 7 or number == 8 or number == 9:
                i = 1
            else:
                i = 0
        return number

    # do not change anything from here to the end
    def get_computer_spot(self):
        index = random.randint(0, self.board.nbr_of_unfilled_slots() - 1)
        nbr = self.board.choose_spot_at(index)
        print('Computer chooses', nbr)
        return nbr

    def start(self):
        print("This program plays tic-tac-toe")
        user_mark = self.get_player_char()
        if user_mark == 'X':  # make sure yourMark is a capital X or O
            computer_mark = 'O'
        else:
            computer_mark = 'X'
        # keep going until somebody has won or the board is full
        while not (self.board.win() or self.board.full()):
            if computer_mark == 'X':  # if computer is X, computer goes first
                index = self.get_computer_spot()
                self.board.setX(index)
                if self.board.full() or self.board.win():
                    break  # is game over before player turn?
                index = self.get_player_spot()  # user goes after computer
                self.board.setO(index)
            else:  # player is X, so goes first
                index = self.get_player_spot()  # user goes first
                self.board.setX(index)
                if self.board.full() or self.board.win():
                    break
                index = self.get_computer_spot()  # then computer if user did not win with last move
                self.board.setO(index)
        self.board.display()
        if self.board.win():
            print(self.board.get_winner() + " wins.")
        else:
            print("Nobody wins.")


if __name__ == "__main__":
    t = TicTacToe()
    t.start()

