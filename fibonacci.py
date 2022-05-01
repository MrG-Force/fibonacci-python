'''
Challenge 1: 
1) Given n, get the nth number in the fibonacci sequence
2) Given a number F, print out whether it's a fibonacci number and what the closest index n in the 
fibonacci sequence is.
"Binet's formula provides a proof that a positive integer x is a Fibonacci number if and only if at least one of 
5 * x * n + 4 or 5 * x * x - 4 is a perfect square". 
Source:
https://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers
'''


# 1)
def get_nth_fibonacci(n):
    generator = generate_fibonacci()
    # discard n - 1 fibonacci numbers
    for _ in range(n - 1):
        next(generator)
    return next(generator)[0]

# 2)


def is_fibonacci(n):
    generator = generate_fibonacci()
    while True:
        fib_n = next(generator)[0]
        if n == fib_n:
            return True
        if n < fib_n:
            return False


def find_closest_fibonacci(n):
    pass
# --- Helper function ---


def generate_fibonacci():
    # Position in the sequence
    nth = 1
    # First two fibonacci numbers
    for i in range(2):
        yield (i, nth)
        nth += 1
    fibn_1 = i
    fibn_2 = 0
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield (next, nth)
        nth += 1
        fibn_2 = fibn_1
        fibn_1 = next


if __name__ == "__main__":
    pass
