import unittest, bubble_serial, insertion_serial, merge_serial, quick_serial

class TestSuite(unittest.TestCase):        

    def setUp(self):
        self.sorted_a = [1, 1, 3, 7, 7, 7, 8, 77]
        self.a = [3, 7, 1, 1, 7, 7, 77, 8]

    def tearDown(self):
        pass

    def test_bubble(self):
        self.assertEqual(bubble_serial.sort(self.a), self.sorted_a)

    def test_insertion(self):
        self.assertEqual(insertion_serial.sort(self.a), self.sorted_a)
    
    def test_merge(self):
        tempa = [0]*len(self.a)
        self.assertEqual(merge_serial.sort(self.a, 0, len(self.a)-1), self.sorted_a)
    
    def test_quick(self):
        self.assertEqual(quick_serial.sort(self.a, 0, len(self.a)-1), self.sorted_a)

if __name__ == '__main__':
    unittest.main()
