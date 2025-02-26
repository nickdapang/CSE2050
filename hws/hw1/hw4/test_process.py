import unittest
from process import Process
class TestProcess(unittest.TestCase):
    def test_create_process_default_cycles(self):
        '''
        Test if creating process with default cycle has the pid, cycles, link, and prev set to the right values.
        '''
        p1 = Process("send_email")
        self.assertEqual(p1.pid, "send_email")
        self.assertEqual(p1.cycles, 100)
        self.assertIsNone(p1.link)
        self.assertIsNone(p1.prev)

    def test_create_process_with_cycles(self):
        '''
        Test if creating process with an input of cycle has the pid, cycles, link, and prev set to the right values.
        '''
        p2 = Process("A", 400)
        self.assertEqual(p2.pid, "A")
        self.assertEqual(p2.cycles, 400)
        self.assertIsNone(p2.link)
        self.assertIsNone(p2.prev)
    
    def test_eq(self):
        '''
        Test if p1 and p2 are equal given the same pid
        '''
        p1 = Process("task1")
        p2 = Process("task1")
        self.assertEqual(p1, p2)
    
    def test_eq(self):
        '''
        test if pid are not equal given different pids
        '''
        p1 = Process('task2')
        p2 = Process("task3")
        self.assertNotEqual(p1, p2)
    
    def test_repr(self):
        '''
        Ensures that the correct string representation is printed when calling the repr function
        '''
        p1 = Process('task1', 1000)
        self.assertEqual(repr(p1), "Process(task1, 150)")

if __name__ == "__main__":
    unittest.main()
