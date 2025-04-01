import unittest
from trib import trib
class test_trib(unittest.TestCase):
    ''' tests that the first ten values would fit the desired values that the trib function returns'''
    def test_first_ten(self):
        solutions = {1:0, 2:0, 3:1, 4:1, 5:2, 6:4, 7:7, 8:13, 9:24, 10: 44}
    
        for k in solutions:
            self.assertEqual(trib(k), solutions[k])
    
    def test_first_100(self):
        '''
        Tests if the 100th number in the sequnece matches the number below
        '''
        k = 100
        self.assertEqual(trib(k), 28992087708416717612934417)

if __name__ == '__main__':
    unittest.main()