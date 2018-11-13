import unittest
from inspect import signature
import sys

from contextlib import contextmanager
from io import StringIO


import get_nbr
import TicTacToe

@contextmanager
def capture_io(input_string=None):
    cap_in = StringIO(input_string)
    cap_out, cap_err = StringIO(), StringIO()
    sys_out, sys_err = sys.stdout, sys.stderr
    sys_in = sys.stdin
    try:
         sys.stdout, sys.stderr = cap_out, cap_err
         sys.stdin = cap_in
         yield sys.stdin, sys.stdout, sys.stderr
    finally:
         sys.stdin = sys_in
         sys.stdout, sys.stderr = sys_out, sys_err



class MyTestCase(unittest.TestCase):
    # test get_player_char(
    def test_get_player_char_exists(self):
        t = TicTacToe.TicTacToe()
        self.assertTrue(hasattr(t, 'get_player_char'),
                        msg='Could not find get_player_char method in TicTacToe class')


    def test_get_player_char_no_params(self):
        self.test_get_player_char_exists()
        t = TicTacToe.TicTacToe()
        self.assertTrue(len(signature(t.get_player_char).parameters)==0,
                        msg='get_player_char method in TicTacToe should have only self as a paramter ')

    def test_get_player_char_X(self):
        self.test_get_player_char_no_params()
        expected = 'X'
        t = TicTacToe.TicTacToe()
        toenter = 'X\n'
        with capture_io(toenter):
            actual = t.get_player_char()
        self.assertEqual(expected, actual,
                         msg='get_player_char should return X when X is entered')

    def test_get_player_char_o(self):
            self.test_get_player_char_no_params()
            expected = 'O'
            t = TicTacToe.TicTacToe()
            toenter = 'o\n'
            with capture_io(toenter):
                actual = t.get_player_char()
            self.assertEqual(expected, actual,
                             msg='get_player_char should return O when o is entered')

    def test_get_player_char_wrongo(self):
        self.test_get_player_char_no_params()
        expected = 'O'
        t = TicTacToe.TicTacToe()
        toenter = 't\nO\n'
        with capture_io(toenter):
            actual = t.get_player_char()
        self.assertEqual(expected, actual,
                         msg='get_player_char should return O when t then O is entered')

    def test_get_player_char_wrongx(self):
        self.test_get_player_char_no_params()
        expected = 'X'
        t = TicTacToe.TicTacToe()
        toenter = 'a\nwer\nret\nx\n'
        with capture_io(toenter):
            actual = t.get_player_char()
        self.assertEqual(expected, actual,
                         msg='get_player_char should return X when errors then X are entered')

#get_player_spot tests. first, test for class and constructor and TicTacToe attribute, given in assignment
    def test_has_TicTacToe_class(self):
        self.assertTrue(hasattr(TicTacToe, 'TicTacToe'),
                        msg='Could not find TicTacToe class in TicTacToe.py')
        # constructor

    def test_has_TicTacToe_constructor(self):
        self.test_has_TicTacToe_class()
        b = TicTacToe.TicTacToe()
        self.assertTrue(hasattr(b, '__init__'),
                        msg='Could not find constructor ("__init__") method in TicTacToe class')

    def test_has_board_attr(self):
        self.test_has_TicTacToe_constructor()
        b = TicTacToe.TicTacToe()
        self.assertTrue(hasattr(b, 'board'),
                        msg='You should have an attribute named board in the TicTacToe class.')

    def test_get_player_spot_exists(self):
        self.test_has_TicTacToe_constructor()
        t = TicTacToe.TicTacToe()
        self.assertTrue(hasattr(t, 'get_player_spot'),
                            msg='Could not find get_player_spot method in TicTacToe class')

    def test_get_player_spot_no_params(self):
        self.test_get_player_spot_exists()
        t = TicTacToe.TicTacToe()
        self.assertTrue(len(signature(t.get_player_spot).parameters) == 0,
                            msg='get_player_spot method in TicTacToe should have only self as a paramter ')

    def test_get_player_spot_3(self):
            self.test_get_player_spot_no_params()
            expected = 3
            t = TicTacToe.TicTacToe()
            toenter = '3\n'
            with capture_io(toenter):
                actual = t.get_player_spot()
            self.assertEqual(expected, actual,
                             msg='get_player_spot should return 3 when 3 is entered')

    def test_get_player_spot_high5(self):
            self.test_get_player_spot_no_params()
            expected = 5
            t = TicTacToe.TicTacToe()
            toenter = '99\n-3\n22\n5\n'
            with capture_io(toenter):
                actual = t.get_player_spot()
            self.assertEqual(expected, actual,
                             msg='get_player_spot should return 5 when 5 is entered')

    def test_get_player_spot_5then6(self):
        self.test_get_player_spot_no_params()
        expected = 6
        t = TicTacToe.TicTacToe()
        t.board.setO(5)
        toenter = '99\n-3\n22\n5\n6'
        with capture_io(toenter):
            actual = t.get_player_spot()
        self.assertEqual(expected, actual)

    def test_get_player_spot_5then6then7(self):
            self.test_get_player_spot_no_params()
            expected = 7
            t = TicTacToe.TicTacToe()
            t.board.setO(5)
            t.board.setX(6)
            toenter = '5\n6\n7'
            with capture_io(toenter):
                actual = t.get_player_spot()
            self.assertEqual(expected, actual)

        #test get_nbr
    def test_getnbr_exists(self):
        self.assertTrue(hasattr(get_nbr, 'get_nbr'),
                        msg='get_nbr function should be in a file called get_nbr.py')

    def test_getnbr_has_string_param(self):
        self.test_getnbr_exists()
        self.assertTrue(len(signature(get_nbr.get_nbr).parameters) == 1,
                        msg='get_nbr function should have one parameter (of type string, a prompt)')

    def test_get_credits_has_return_value(self):
        toenter = '3\n'
        with capture_io(toenter):
            actual = get_nbr.get_nbr('hello')
        self.assertIsNotNone(actual,
                             msg="get_nbr.get_nbr('Enter a number-> ') returned None. Make sure you have a return.")

    def test_getnbr_valid(self):
        toenter = '3\n'
        expected = 3
        with capture_io(toenter):
            actual = get_nbr.get_nbr('hello')
        self.assertEqual(expected, actual,
                         msg='get_nbr.get_nbr("Enter a number-> ") should return 3 when 3 is entered')

    def test_getnbr__some_invalid(self):
        toenter = 'a\n15f\n45\n'
        expected = 45
        with capture_io(toenter):
            actual = get_nbr.get_nbr('hello')
        self.assertEqual(expected, actual,
                         msg="get_nbr.get_nbr('Enter a number-> ') should return 45, the last value and only number entered.")

    def test_getnbr__one_invalid(self):
        toenter = 'a3\n5\n'
        expected = 5
        with capture_io(toenter):
            actual = get_nbr.get_nbr('hello')
        self.assertEqual(expected, actual,
                         msg="get_nbr.get_nbr('Enter a number-> ') should return 5, the last value and only number entered.")


if __name__ == '__main__':
    unittest.main()
