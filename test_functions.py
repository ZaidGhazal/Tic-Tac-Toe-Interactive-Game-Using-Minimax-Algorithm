import unittest

from tictactoe import actions, player, result

X = "X"
O = "O"
EMPTY = None

class testTicTacToe(unittest.TestCase):
        """This class tests the functions in tictactoe.py """

        def test_player(self):
                """This function tests the player function in tictactoe.py """
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
                """This function tests the actions function in tictactoe.py """
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

        def test_result(self):
                """This function tests the result function in tictactoe.py """
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
                
                self.assertEqual(result(board_1, (2,2)), 
                        [[EMPTY, X, O],
                        [EMPTY, X, O],
                        [EMPTY, EMPTY, X]])
                self.assertEqual(result(board_2, (0,0)), [[O, X, O],
                        [X, X, O],
                        [EMPTY, EMPTY, EMPTY]])
                self.assertRaises(Exception, result, board_3, (0,0))
                self.assertEqual(result(board_4, (1,1)), [[EMPTY, EMPTY, EMPTY],
                        [EMPTY, X, EMPTY],
                        [EMPTY, EMPTY, EMPTY]])
