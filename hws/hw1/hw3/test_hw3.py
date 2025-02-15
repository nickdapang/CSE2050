import unittest
import hw3
class testhw3(unittest.TestCase):
    
    def test_generate_lists(self):
        '''
        Description: Checks if the generate_lists function returns a list of length of the desired size as well 
        as if every item in the list is unqiue

        '''
        size = 10
        result = hw3.generate_lists(size)
        self.assertEqual(len(result[0]), size)
        self.assertEqual(len(result[1]), size)
        set1 = set(result[0])
        set2 = set(result[1])
        self.assertEqual(len(set1), size)
        self.assertEqual(len(set2), size)
    
    def test_find_common(self):
        '''
        Description: Tests if the find_common function returns the correct amount of elements that are common between
        the two lists by adding the two list and subtracting it from the set, getting the elements that are duplicated
        '''
        size = 10
        result = hw3.generate_lists(size)
        result1 = hw3.find_common(result[0], result[1])
        list = result[0] + result[1]
        set1 = set(list)
        count = len(result[0]) + len(result[1]) - len(set1) 
        self.assertEqual(result1, count)

    def test_find_common_efficient(self):
        '''
        Description: Tests if the find_common_efficient function returns the correct amount of elements that are common between
        the two lists by adding the two list and subtracting it from the set, getting the elements that are duplicated
        '''
        size = 10
        result = hw3.generate_lists(size)
        result1 = hw3.find_common_efficient(result[0], result[1])
        list = result[0] + result[1]
        set1 = set(list)
        count = len(result[0]) + len(result[1]) - len(set1)
        self.assertEqual(result1, count)

if __name__ == '__main__':
    unittest.main()