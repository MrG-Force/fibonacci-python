import unittest
import fibonacci as fib


class TestFibonacci(unittest.TestCase):

    def test_get_nth_fibonacci(self):
        self.assertEqual(fib.get_nth_fibonacci(10), 34, "Expected 34")
        self.assertEqual(fib.get_nth_fibonacci(1), 0, "Expected 0")

    def test_is_fibonacci(self):
        self.assertTrue(fib.is_fibonacci(377))
        self.assertFalse(fib.is_fibonacci(378))

    def test_find_closest_fibonacci(self):
        self.assertEquals(fib.find_closest_fibonacci(
            12), 8, "Closest number to 12 in the fibonacci sequence is at the 8th position -> 13")


if __name__ == '__main__':
    unittest.main()
