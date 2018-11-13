import random
from board_class import Board
from get_nbr import get_nbr

#Note: This file will not compile as is because there are methods missing

class TicTacToe:
     # put constructor here


     # put get_player_char here

    # put get_player_spot here

    # do not change anything from here to the end
    def get_computer_spot(self):
        index = random.randint(0,self.board.nbr_of_unfilled_slots()-1)
        nbr = self.board.take_spot_at(index)
        print('Computer chooses',nbr)
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
                index = self.get_player_spot() #user goes after computer
                self.board.setO(index)
            else:  # player is X, so goes first
                index = self.get_player_spot() #user goes first
                self.board.setX(index)
                if self.board.full() or self.board.win():
                    break
                index = self.get_computer_spot() # then computer if user did not win with last move
                self.board.setO(index)
        self.board.display()
        if self.board.win():
                print(self.board.get_winner() + " wins.")
        else:
             print("Nobody wins.")

if __name__ == "__main__":
    t = TicTacToe()
    t.start()
