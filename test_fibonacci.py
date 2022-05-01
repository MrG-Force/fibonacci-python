import unittest
import fibonacci as fib


class TestFibonacci(unittest.TestCase):

    def test_get_nth_fibonacci(self):
        self.assertEqual(fib.get_nth_fibonacci(10), 55, "Expected 55")


if __name__ == '__main__':
    unittest.main()
