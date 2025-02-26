import unittest
from process import Process
from circularqueue import CircularQueue

class TestCircularQueue(unittest.TestCase):
    def test_init_empty(self):
        '''
        Description: Initalize an empty CQ and test it
        '''
        cq = CircularQueue()
        self.assertEqual(len(cq), 0)
        self.assertIsNone(cq._head)

    def test_init_Process(self):
        '''
        Description: Initialize A CQ with a list of Process objects
        '''
        p1 = Process('s')
        p2 = Process('l')
        cq = CircularQueue([p1,p2])
        self.assertEqual(len(cq), 2)
        self.assertEqual(cq._head.pid, 's')
    
    def test_add_process_one(self):
        cq = CircularQueue()
        p1 = Process('a')
        cq.add_process(p1)
        self.assertEqual(len(cq), 1)
        self.assertEqual(cq._head.pid, 'a')
    
    def test_add_process_two(self):
        cq = CircularQueue()
        p1 = Process('b')
        p2 = Process('a')
        cq.add_process(p1)
        cq.add_process(p2)
        self.assertEqual(len(cq), 2)
        self.assertEqual(cq._head.pid, 'b')
    
    def test_add_process_three(self):
        cq = CircularQueue()
        p1 = Process('A')
        p2 = Process('B')
        p3 = Process('C')
        cq.add_process(p1)
        cq.add_process(p2)
        cq.add_process(p3)
        self.assertEqual(len(cq), 3)
        self.assertEqual(cq._head.pid, 'A')
    
    def test_repr(self):
        p1 = Process('a')
        p2 = Process('b')
        p3 = Process('c')
        cq = CircularQueue([p1,p2,p3])
        self.assertEqual(repr(cq), 'CircularQueue(Process(a 100), Process(b 100), Process(c 100))')
    
    def test_remove_process_middle(self):
        p1 = Process('a')
        p2 = Process('b')
        p3 = Process('c')
        cq = CircularQueue([p1,p2,p3])
        cq.remove_process(p2)
        self.assertEqual(len(cq), 2)
        self.assertEqual(cq._head.link.pid, 'c')
    
    def test_remove_process_front(self):
        p1 = Process('a')
        p2 = Process('b')
        p3 = Process('c')
        cq = CircularQueue([p1,p2,p3])
        cq.remove_process(p1)
        self.assertEqual(len(cq), 2)
        self.assertEqual(cq._head.pid, 'b')
    
    def test_remove_process_end(self):
        p1 = Process('a')
        p2 = Process('b')
        p3 = Process('c')
        cq = CircularQueue([p1,p2,p3])
        cq.remove_process(p3)
        self.assertEqual(len(cq), 2)
        self.assertEqual(cq._head.link.link, cq._head)

    def test_kill(self):
        '''
        Description:
        '''
        p1 = Process('a')
        p2 = Process('b')
        p3 = Process('c')
        cq = CircularQueue([p1,p2,p3])
        killed = cq.kill('b')
        self.assertEqual(killed.pid, 'b')
        self.assertEqual(len(cq), 2)

if __name__ == '__main__':
    unittest.main()