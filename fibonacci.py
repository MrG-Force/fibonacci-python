'''
Challenge: 
1) Given n, get the nth number in the fibonacci sequence
2) Given a number F, print out whether it's a fibonacci number and what the closest index n in the 
fibonacci sequence is.
"Binet's formula provides a proof that a positive integer x is a Fibonacci number if and only if at least one of 
5 * x * n + 4 or 5 * x * x - 4 is a perfect square". 
Source:
https://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers
'''
import argparse
import textwrap


def main():
    args = get_args()
    if args.find:
        try:
            if args.Number == 0:
                raise argparse.ArgumentTypeError
        except argparse.ArgumentTypeError:
            print("0 is not a valid index in a 1-based sequence")
            return

        if args.verbose:
            print(
                f"The {args.Number}{get_ord_sufx(args.Number)} number in the Fibonacci sequence is: {get_nth_fibonacci(args.Number)}")
        print(f"{args.Number}th Fibonacci: {get_nth_fibonacci(args.Number)}")

    else:
        result = is_fibonacci(args.Number)
        if result[0]:
            if args.verbose:
                print(
                    f"{args.Number} is at the {result[1]}{get_ord_sufx(result[1])} position in the Fibonacci sequence.")
            else:
                print(
                    f"{result[0]}, ({result[1]}{get_ord_sufx(result[1])}: {args.Number})")
        else:
            closest = find_closest_fibonacci(args.Number)
            if args.verbose:
                print(
                    f"{args.Number} is not in the Fibonacci sequence," +
                    f" the closest Fibonacci number is {closest[0]} at the {closest[1]}{get_ord_sufx(closest[1])} index.")
            else:
                print(
                    f"{result[0]}, ({closest[1]}{get_ord_sufx(closest[1])}: {closest[0]})")


# 1)
def get_nth_fibonacci(n):
    gen = generate_fibonacci()
    # discard range(n - 1) fibonacci numbers
    for _ in range(n - 1):
        next(gen)
    return next(gen)[0]

# 2)


def is_fibonacci(n):
    gen = generate_fibonacci()

    while True:
        fib = next(gen)
        fib_num = fib[0]
        fib_indx = fib[1]

        if n == fib_num:
            return (True, fib_indx)
        if n < fib_num:
            return (False, -1)


def find_closest_fibonacci(n):
    gen = generate_fibonacci()
    fib_last = next(gen)

    while fib_last[0] < n:
        fib_prev = fib_last
        fib_last = next(gen)

    difference_prev = abs(fib_prev[0] - n)
    difference_last = abs(fib_last[0] - n)

    if difference_last < difference_prev:
        return fib_last
    return fib_prev


# --- Helper functions ---

def generate_fibonacci() -> tuple:
    # Position in the sequence
    pos = 1
    # First two fibonacci numbers
    for i in range(2):
        yield (i, pos)
        pos += 1

    fibn_1 = i
    fibn_2 = 0
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield (next, pos)  # (fibonacci_number, its_position)
        pos += 1
        fibn_2 = fibn_1
        fibn_1 = next


def check_positive(number):
    if int(number) < 0:
        raise argparse.ArgumentTypeError("Not a valid int >= 0")
    return int(number)


def get_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
            This program has two main functionalities:
                1. Given an index n (1-based), return the corresponding number at the nth position in the Fibonacci sequence.
                    e.g.: fibonacci.py 4 --find -> 2.
                2. Given a number n, determine whether it is a fibonacci number and, if not, find what is the closest index in the fibonacci sequence.
                    e.g.: fibonacci.py 54 --check -> "False, ('11th': 55)" '''))
    num_group = parser.add_mutually_exclusive_group(required=True)
    num_group.add_argument("-f", "--find", action="store_true",
                           help="To find a number at the given position in the Fibonacci sequence")
    num_group.add_argument("-c", "--check", action="store_true",
                           help="To determine whether n is a Fibonacci number")
    parser.add_argument("Number", help="An integer", type=check_positive)
    parser.add_argument("-v", "--verbose",
                        help="Display a verbose output", action="store_true")
    return parser.parse_args()


def get_ord_sufx(number):
    teen = number % 100
    if teen in [11, 12, 13]:
        return "th"
    last = number % 10
    if last == 1:
        return "st"
    if last == 2:
        return "nd"
    if last == 3:
        return "rd"
    return "th"


if __name__ == "__main__":
    main()
