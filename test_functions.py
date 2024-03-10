import unittest

from tictactoe import actions, player, result, terminal, winner

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

        def test_terminal(self):
                """This function tests the terminal function in tictactoe.py """
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
                
                self.assertEqual(terminal(board_1), False)
                self.assertEqual(terminal(board_2), False)
                self.assertEqual(terminal(board_3), True)
                self.assertEqual(terminal(board_4), False)
        
        def test_winner(self):
                """This function tests the winner function in tictactoe.py """
                board_1 = [[EMPTY, X, O],
                        [EMPTY, X, O],
                        [EMPTY, EMPTY, EMPTY]]
                
                board_2 = [[EMPTY, X, O],
                           [EMPTY, X, O],
                           [EMPTY, X, EMPTY]]
                
                board_3 = [     [O, O, X],
                                [O, X, EMPTY],
                                [X, EMPTY, X]]
                
                board_4 = [[EMPTY, EMPTY, EMPTY],
                        [EMPTY, EMPTY, EMPTY],
                        [EMPTY, EMPTY, EMPTY]]
                
                board_5 = [     [O, O, O],
                                [X, X, O],
                                [X, X, EMPTY]]
                
                self.assertEqual(winner(board_1), None)
                self.assertEqual(winner(board_2), X)
                self.assertEqual(winner(board_3), X)
                self.assertEqual(winner(board_4), None)
                self.assertEqual(winner(board_5), O)

