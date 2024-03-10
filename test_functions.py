import unittest

from tictactoe import actions, player

X = "X"
O = "O"
EMPTY = None

class testTicTacToe(unittest.TestCase):
    

    def test_player(self):

        board_1 = [[EMPTY, X, O],
                [EMPTY, X, O],
                [EMPTY, EMPTY, EMPTY]]
        
        board_2 = [[EMPTY, X, O],
                [X, X, O],
                [EMPTY, EMPTY, EMPTY]]
        board_3 = [ [O, X, O],
                    [X, X, O],
                    [X, O, X]]
        board_4 = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        
        self.assertEqual(player(board_1), X)
        self.assertEqual(player(board_2), O)
        self.assertIn(player(board_3), [O, X])
        self.assertEqual(player(board_4), X)

    def test_actions(self):

        board_1 = [[EMPTY, X, O],
                [EMPTY, X, O],
                [EMPTY, EMPTY, EMPTY]]
        
        board_2 = [[EMPTY, X, O],
                [X, X, O],
                [EMPTY, EMPTY, EMPTY]]
        board_3 = [ [O, X, O],
                    [X, X, O],
                    [X, O, X]]
        board_4 = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        
        self.assertEqual(actions(board_1), set([(0,0), (1,0), (2,0), (2,1), (2,2)]))
        self.assertEqual(actions(board_2), set([(0,0), (2,0), (2,1), (2,2)]))
        self.assertEqual(actions(board_3), set())
        self.assertEqual(actions(board_4), set([(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]))
        
