import unittest
import fibonacci as fib


class TestFibonacci(unittest.TestCase):

    def test_get_nth_fibonacci(self):
        self.assertEqual(fib.get_nth_fibonacci(10), 34, "Expected 34")
        self.assertEqual(fib.get_nth_fibonacci(1), 0, "Expected 0")

    def test_is_fibonacci(self):
        self.assertTrue(fib.is_fibonacci(377))
        self.assertFalse(fib.is_fibonacci(378))


if __name__ == '__main__':
    unittest.main()
