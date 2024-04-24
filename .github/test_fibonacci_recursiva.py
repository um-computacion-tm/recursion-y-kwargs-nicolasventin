import unittest

from fibonacci_recursiva import fibonacci

class testseriedefibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        result = fibonacci(0)
        self.assertEqual(result, 0)

    def test_fibonacci_1(self):
        result = fibonacci(1)
        self.assertEqual(result, 1)

    def test_fibonacci_2(self):
        result = fibonacci(2)
        self.assertEqual(result, 1)    

    def test_fibonacci_3(self):
        result = fibonacci(3)
        self.assertEqual(result, 2)
    
    def test_fibonacci_4(self):
        result = fibonacci(4)
        self.assertEqual(result, 3)

    def test_fibonacci_5(self):
        result = fibonacci(5)
        self.assertEqual(result, 5)

    def test_fibonacci_6(self):
        result = fibonacci(6)
        self.assertEqual(result, 8)
    
    def test_fibonacci_7(self):
        result = fibonacci(7)
        self.assertEqual(result, 13)

    def test_fibonacci_8(self):
        result = fibonacci(8)
        self.assertEqual(result, 21)



if __name__ == "__main__":
    unittest.main()