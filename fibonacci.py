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


def main():
    find_closest_fibonacci(12)


# 1)
def get_nth_fibonacci(n):
    gen = generate_fibonacci()
    # discard n - 1 fibonacci numbers
    for _ in range(n - 1):
        next(gen)
    return next(gen)[0]

# 2)


def is_fibonacci(n):
    gen = generate_fibonacci()

    while True:
        fib_n = next(gen)[0]

        if n == fib_n:
            return True
        if n < fib_n:
            return False


def find_closest_fibonacci(n):
    gen = generate_fibonacci()
    fib_last = next(gen)

    while fib_last[0] < n:
        fib_prev = fib_last
        fib_last = next(gen)

    difference_prev = abs(fib_prev[0] - n)
    difference_last = abs(fib_last[0] - n)

    if difference_last < difference_prev:
        return fib_last[1]
    return fib_prev[1]


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
    main()
