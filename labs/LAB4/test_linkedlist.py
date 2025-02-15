from linkedlist import LinkedList 
import unittest

class test_linkedlist(unittest.TestCase):
    def test_linkedlist(self):
        '''
        Checks if the linked list
        '''
        LL1 = LinkedList()
        self.assertEqual(len(LL1), 0)
        self.assertIsNone(LL1.get_head())
        self.assertIsNone(LL1.get_tail())


    def test_add_last(self):
        ll = LinkedList()
        items = ['a', 'b', 'c']

        for i in range(len(items)):
            ll.add_last(items[i])
            self.assertEqual(len(ll), i + 1)
            self.assertEqual(ll.get_head(), 'a')
            self.assertEqual(ll.get_tail(), items[i])
    
    def test_nonemptyinit(self):
        ll = LinkedList('a','b', 'c')
        self.assertEqual(ll.get_head, 'a')
        self.assertEqual(ll.get_tail, 'c')
        self.assertEqual(len(ll), 3)


    def test_add_first(self):
        ll = LinkedList()
        items = ['a', 'b', 'c']
        for i in range(len(items)):
            ll.add_first(items[i])
            self.assertEqual(len(ll), i + 1)
            self.assertEqual(ll.get_head(), items[i])
            self.assertEqual(ll.get_tail(), 'a')

    
    def test_remove_last(self):
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
