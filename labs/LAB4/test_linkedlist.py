from linkedlist import LinkedList 
import unittest

class test_linkedlist(unittest.TestCase):
    def test_linkedlist(self):
        '''
        Checks if the linked list with len 0 returns None for head and tail
        '''
        LL1 = LinkedList()
        self.assertEqual(len(LL1), 0)
        self.assertIsNone(LL1.get_head())
        self.assertIsNone(LL1.get_tail())


    def test_add_last(self):
        '''
        Desciption: Each time you call add_last
        this function checks if the length, the tail, and the head
        returns the right information
        '''
        ll = LinkedList()
        items = ['a', 'b', 'c']

        for i in range(len(items)):
            ll.add_last(items[i])
            self.assertEqual(len(ll), i + 1)
            self.assertEqual(ll.get_head(), 'a')
            self.assertEqual(ll.get_tail(), items[i])
    
    def test_nonemptyinit(self):
        '''
        Description: checks if the tail, head, and length of the list returns correct information
        '''
        ll = LinkedList(['a','b', 'c'])
        self.assertEqual(ll.get_head(), 'a')
        self.assertEqual(ll.get_tail(), 'c')
        self.assertEqual(len(ll), 3)


    def test_add_first(self):
        '''
        Description: Each time you call the add_first function
        this function tests if the length and head of the linked list is equal
        '''
        ll = LinkedList()
        items = ['a', 'b', 'c']
        for i in range(len(items)):
            ll.add_first(items[i])
            self.assertEqual(len(ll), i + 1)
            self.assertEqual(ll.get_head(), items[i])
            self.assertEqual(ll.get_tail(), 'a')

    
    def test_remove_last(self):
        '''
        Description: every time you call the remove_last function, you check if teh head and tail returns the right information
        '''
        ll = LinkedList()
        data = ['a', 'b', 'c']
        for i in range(len(data)):
            ll.add_last(data[i])
        
        for i in range(len(data)):
            self.assertEqual(len(ll), 3 - i)
            self.assertEqual(ll.get_head(), data[0])
            self.assertEqual(ll.get_tail(), data[len(ll) - 1])
            
            old_tail = ll.remove_last()
            self.assertEqual(old_tail, data[2-i])

if __name__ == '__main__':
    unittest.main()
