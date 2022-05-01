'''
Challenge 1: 
1) Given n, get the nth number in the fibonacci sequence
2) Alternatively given a number F, print out whether it's a fibonacci number and what the closest index n in the 
fibonacci sequence is.
"Binet's formula provides a proof that a positive integer x is a Fibonacci number if and only if at least one of 
5 * x * n + 4 or 5 * x * x - 4 is a perfect square". 
Source:
https://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers
'''


# 1)
def get_nth_fibonacci(n):
    pass


def test_get_nth_fibonacci():
    assert get_nth_fibonacci(10) == 55, "Should return 55"


if __name__ == "__main__":
    test_get_nth_fibonacci()
    print("All sweet!")
