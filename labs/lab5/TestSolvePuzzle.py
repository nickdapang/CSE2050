import solvepuzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                L = [3,6,4,1,3,4,2,0]
                self.assertTrue(solvepuzzle.solve_puzzle(L))
        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                L = [3,3,2,4,2,0]
                self.assertTrue(solvepuzzle.solve_puzzle(L))
        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                L = [3,6,3,1,4,4,2,0]
                self.assertTrue(solvepuzzle.solve_puzzle(L))
        def testUnsolveable(self):
                """Tests an unsolveable board"""
                L = [3,4,1,2,0]
                self.assertFalse(solvepuzzle.solve_puzzle(L))
unittest.main()