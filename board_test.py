import unittest
from inspect import signature
import board_class
class MyTestCase(unittest.TestCase):

    def test_has_Board_class(self):
        self.assertTrue(hasattr(board_class, 'Board'),
                        msg='Could not find Board class in board.py')
#constructor
    def test_has_Board_constructor(self):
        self.test_has_Board_class()
        b = board_class.Board()
        self.assertTrue(hasattr(b, '__init__'),
                        msg='Could not find constructor ("__init__") method in Board class')

    def test_has_SIZE_attr(self):
        self.test_has_Board_constructor()
        b = board_class.Board()
        self.assertTrue(hasattr(b, 'SIZE'),
                        msg='You should have an attribute named SIZE in the Board class. It should have the value 9.')


#test nbr_of_unfilled_slots
    def test_has_unfilled_slots(self):
        self.test_has_Board_constructor()
        b = board_class.Board()
        self.assertTrue(hasattr(b, 'nbr_of_unfilled_slots'),
                        msg='Could not find nbr_of_unfilled_slots method in Board class')


    def test_unfilled_no_params(self):
        self.test_has_unfilled_slots()
        b = board_class.Board()
        self.assertTrue(len(signature(b.nbr_of_unfilled_slots).parameters)==0,
                        msg='The nbr_of_unfilled_slots method in Board should have a self parameter only')


    def test_unfilled_all(self):
        self.test_unfilled_no_params()
        b = board_class.Board()
        actual = b.nbr_of_unfilled_slots()
        expected = b.SIZE
        self.assertEqual(expected, actual)


    def test_unfilled_none(self):
            self.test_unfilled_no_params()
            b = board_class.Board()
            for i in range(1,b.SIZE+1):
                b.take_spot(i)
            actual = b.nbr_of_unfilled_slots()
            expected = 0
            self.assertEqual(expected, actual)

    def test_unfilled_some(self):
        self.test_unfilled_no_params()
        b = board_class.Board()
        b.take_spot(2)
        b.take_spot(9)
        b.take_spot(8)
        b.take_spot(7)
        actual = b.nbr_of_unfilled_slots()
        expected = b.SIZE-4
        self.assertEqual(expected, actual, msg='The take_spot method in Board should have a self and an integer parameter. It does not.')


        #test take_spot
    def test_Board_has_take_spot(self):
        self.test_has_Board_constructor()
        b = board_class.Board()
        self.assertTrue(hasattr(b, 'take_spot'),
                        msg='Could not find take_spot method in Board class')

    def test_Board_take_one_param(self):
        self.test_Board_has_take_spot()
        b = board_class.Board()
        self.assertTrue(len(signature(b.take_spot).parameters)==1,
                        msg='The take_spot method in Board should have a self and an integer parameter. It does not.')


    def test_Board_take_spot3_list(self):
        self.test_Board_take_one_param()
        b = board_class.Board()
        b.take_spot(3)
        actual = b.spots_left
        expected = [1, 2, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected, actual)


    def test_Board_take_spot1(self):
        self.test_Board_take_one_param()
        b = board_class.Board()
        b.take_spot(1)
        actual = b.spots_left
        expected = [2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected, actual)

    def test_Board_take_spot9(self):
        self.test_Board_take_one_param()
        b = board_class.Board()
        b.take_spot(9)
        actual = b.spots_left
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(expected, actual)



 #choose_spot_at
    def test_Board_has_choose_spot_at(self):
        self.test_has_Board_constructor()
        b = board_class.Board()
        self.assertTrue(hasattr(b, 'choose_spot_at'),
                    msg='Could not find choose_spot_at method in Board class')


    def test_Board_choose_one_param(self):
        self.test_Board_has_choose_spot_at()
        b = board_class.Board()
        self.assertTrue(len(signature(b.choose_spot_at).parameters) == 1,
                    msg='The choose_spot_at method in Board should have a self and an integer parameter. It does not.')

    def test_choose_spot_last(self):
        self.test_Board_choose_one_param()
        b = board_class.Board()
        expected = 9
        actual = b.choose_spot_at(8)
        self.assertEqual(expected, actual)

    def test_choose_spot_last_after_one_del(self):
        self.test_Board_choose_one_param()
        b = board_class.Board()
        b.take_spot(3)
        expected = 9
        actual = b.choose_spot_at(7)
        self.assertEqual(expected, actual)


    def test_choose_spot_third_after_two_del(self):
        self.test_Board_choose_one_param()
        b = board_class.Board()
        b.take_spot(3)
        b.take_spot(6)
        expected = 7
        actual = b.choose_spot_at(4)
        self.assertEqual(expected, actual, msg="After removing 3 and 6, the list should be 1, 2, 4, 5, 7, 8, 9. Index 4 holds 7.")

    def test_choose_spot_first_after_two_del(self):
        self.test_Board_choose_one_param()
        b = board_class.Board()
        b.take_spot(3)
        b.take_spot(6)
        expected = 1
        actual = b.choose_spot_at(0)
        self.assertEqual(expected, actual, msg="After removing 3 and 6, the list should be 1, 2, 4, 5, 7, 8, 9. Index 0 holds 1.")


#setX and setO tests
    def test_setX_exists(self):
            self.test_has_Board_constructor()
            b = board_class.Board()
            self.assertTrue(hasattr(b, 'setX'),
                            msg='Could not find the setX method in Board class')



    def test_setO_exists(self):
            self.test_has_Board_constructor()
            b = board_class.Board()
            self.assertTrue(hasattr(b, 'setO'),
                            msg='Could not find the setO method in Board class')

    def test_setX_one_param(self):
        self.test_setX_exists()
        b = board_class.Board()
        self.assertTrue(len(signature(b.setX).parameters) == 1,
                    msg='The setX method in Board should have a self and an integer parameter. It does not.')


    def test_setO_one_param(self):
        self.test_setO_exists()
        b = board_class.Board()
        self.assertTrue(len(signature(b.setO).parameters) == 1,
                    msg='The setOmethod in Board should have a self and an integer parameter. It does not.')

    def test_setX_1(self):
        self.test_setX_one_param()
        b = board_class.Board()
        b.setX(1)
        expected = ['X', 'N', 'N','N','N','N','N','N','N' ]
        actual = b.board
        self.assertEqual(expected, actual,
                         msg="After setting the first spot to be X, board[0] should be X, and all others BLANK")

    def test_setO_1(self):
        self.test_setO_one_param()
        b = board_class.Board()
        b.setO(1)
        expected = ['O', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
        actual = b.board
        self.assertEqual(expected, actual,
                         msg="After setting the first spot to be O, board[0] should be O, and all others BLANK")

    def test_setX_3(self):
            self.test_setX_one_param()
            b = board_class.Board()
            b.board = ['O', 'X', 'N', 'N', 'N', 'O', 'X', 'N', 'N']
            b.setX(3)
            expected = ['O', 'X', 'X', 'N', 'N', 'O', 'X', 'N', 'N']
            actual = b.board
            self.assertEqual(expected, actual)


    def test_setO_3(self):
            self.test_setX_one_param()
            b = board_class.Board()
            b.board = ['O', 'X', 'N', 'N', 'N', 'O', 'X', 'N', 'N']
            b.setO(3)
            expected = ['O', 'X', 'O', 'N', 'N', 'O', 'X', 'N', 'N']
            actual = b.board
            self.assertEqual(expected, actual)

        #get_winner tests
    def test_has_get_winner(self):
        self.test_has_Board_constructor()
        b = board_class.Board()
        self.assertTrue(hasattr(b, 'get_winner'),
                            msg='Could not find the get_winner method in Board class')

    def test_getwin_has_zero_param(self):
            self.test_has_get_winner()
            b = board_class.Board()
            self.assertTrue(len(signature(b.get_winner).parameters) == 0,
                            msg='The get_winner method in Board should not have any user parameters.')

    def test_get_winner_blanks(self):
        self.test_has_get_winner()
        b = board_class.Board()
        expected = b.BLANK
        actual = b.get_winner()
        self.assertEqual(expected, actual, msg="get_winner should return Blank before anybody has played.")

    def test_get_winner_blanks2(self):
        self.test_has_get_winner()
        b = board_class.Board()
        b.board = ['O', 'N', 'X', 'X', 'N', 'O', 'O', 'N', 'N']
        expected = b.BLANK
        actual = b.get_winner()
        self.assertEqual(expected, actual, msg="get_winner should return Blank if there are no winners yet.")

# first row
    def test_get_winner_row1(self):
        self.test_has_get_winner()
        b = board_class.Board()
        b.board = ['O', 'O', 'O', 'X', 'N', 'N', 'N', 'N', 'N']
        expected = 'O'
        actual = b.get_winner()
        self.assertEqual(expected, actual, msg="if top row is 3 Os, O should be a winner")

   #third row
    def test_get_winner_row3(self):
        self.test_has_get_winner()
        b = board_class.Board()
        b.board = [ 'X', 'N', 'N', 'N', 'N', 'N', 'X', 'X', 'X']
        expected = 'X'
        actual = b.get_winner()
        self.assertEqual(expected, actual, msg="if bottow row is 3 Xs, X should be a winner")

        # second column

    def test_get_winner_col_2(self):
        self.test_has_get_winner()
        b = board_class.Board()
        b.board = ['N', 'X', 'N', 'N', 'X', 'N', 'O', 'X', 'X']
        expected = 'X'
        actual = b.get_winner()
        self.assertEqual(expected, actual, msg="if middle column row is 3 Xs, X should be a winner")

# 0 diagonal
    def test_get_winner_diag_0(self):
        self.test_has_get_winner()
        b = board_class.Board()
        b.board = ['O', 'X', 'N', 'N', 'O', 'N', 'O', 'X', 'O']
        expected = 'O'
        actual = b.get_winner()
        self.assertEqual(expected, actual, msg="if diagonal down is 3 Os, O should be a winner")

# cat
    def test_get_winner_cat(self):
        self.test_has_get_winner()
        b = board_class.Board()
        b.board = ['X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O']
        expected = b.BLANK
        actual = b.get_winner()
        self.assertEqual(expected, actual, msg="In no winner games, get_winner should return N ")


# testing win
    def test_has_win(self):
        self.test_has_Board_constructor()
        b = board_class.Board()
        self.assertTrue(hasattr(b, 'win'),
                            msg='Could not find the win method in Board class')

    def test_getwin_has_zero_param(self):
            self.test_has_win()
            b = board_class.Board()
            self.assertTrue(len(signature(b.win).parameters) == 0,
                            msg='The win method in Board should not have any user parameters.')

    def test_win_blanks(self):
        self.test_has_win()
        b = board_class.Board()
        actual = b.win()
        self.assertFalse(actual, msg="win should return False before anybody has played.")

    def test_win_blanks2(self):
        self.test_has_win()
        b = board_class.Board()
        b.board = ['O', 'N', 'X', 'X', 'N', 'O', 'O', 'N', 'N']
        actual = b.win()
        self.assertFalse(actual, msg="win should return False if there are no winners yet.")

# second row
    def test_win_row_2(self):
        self.test_has_win()
        b = board_class.Board()
        b.board = [ 'X', 'N', 'N', 'O', 'O', 'O','N', 'N', 'N']
        actual = b.win()
        self.assertTrue(actual, msg="if middle row is 3 Os, win should return true")

   #first column
    def test_win_col_1(self):
        self.test_has_win()
        b = board_class.Board()
        b.board = [ 'X', 'N', 'N', 'X', 'N', 'N', 'X', 'N', 'X']
        actual = b.win()
        self.assertTrue(actual, msg="if first column is 3 Xs, win should return true")

        # third column
    def test_win_col3(self):
        self.test_has_win()
        b = board_class.Board()
        b.board = ['N', 'N', 'X', 'N', 'N', 'X', 'N', 'O', 'X']
        actual = b.win()
        self.assertTrue(actual, msg="if last column row is 3 Xs, win should return true")

# last diagonal
    def test_win_blanks6(self):
        self.test_has_win()
        b = board_class.Board()
        b.board = ['N', 'N', 'O', 'X',  'O', 'N', 'O', 'X', 'O']
        actual = b.win()
        self.assertTrue(actual, msg="if end diagonal down is 3 Os, win should return true")

#testing full
    def test_full_exists(self):
        self.test_has_Board_constructor()
        b = board_class.Board()
        self.assertTrue(hasattr(b, 'full'),
                    msg='Could not find the full method in Board class')


    def test_full_has_zero_param(self):
        self.test_full_exists()
        b = board_class.Board()
        self.assertTrue(len(signature(b.full).parameters) == 0,
                    msg='The full method in Board should not have any user parameters.')

    def test_full_empty(self):
        self.test_full_has_zero_param()
        b = board_class.Board()
        actual = b.full()
        self.assertFalse(actual, msg="When the board has no Xs or Os, full should return False")

    def test_full_full(self):
        self.test_full_has_zero_param()
        b = board_class.Board()
        for i in range(1,b.SIZE+1):
            b.setO(i)
        actual = b.full()
        self.assertTrue(actual, msg="When the board is all Xs or Os, full should return True")

    def test_full_half_full(self):
        self.test_full_has_zero_param()
        b = board_class.Board()
        for i in range(1, b.SIZE + 1,2):
            b.setX(i)
        actual = b.full()
        self.assertFalse(actual, msg="When the board has only some Xs and Os, full should return False")


if __name__ == '__main__':
            unittest.main()
