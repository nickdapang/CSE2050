import unittest
from process import Process
class TestProcess(unittest.TestCase):
    def test_create_process_default_cycles(self):
        p1 = Process("send_email")
        self.assertEqual(p1.pid, "send_email")
        self.assertEqual(p1.cycles, 100)
        self.assertIsNone(p1.link)
        self.assertIsNone(p1.prev)

    def test_create_process_with_cycles(self):
        p2 = Process("A", 400)
        self.assertEqual(p2.pid, "A")
        self.assertEqual(p2.cycles, 400)
        self.assertIsNone(p2.link)
        self.assertIsNone(p2.prev)
    
    def test_eq(self):
        p1 = Process("task1")
        p2 = Process("task1")
        self.assertEqual(p1, p2)
    
    def test_eq(self):
        p1 = Process('task2')
        p2 = Process("task3")
        self.assertNotEqual(p1, p2)
    
    def test_repr(self):
        p1 = Process('task1', 1000)
        self.assertEqual(repr(p1), "Process(task1, 150)")

if __name__ == "__main__":
    unittest.main()
