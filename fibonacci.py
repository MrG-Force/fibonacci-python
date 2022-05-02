'''
Challenge: 
1) Given n, get the nth number in the fibonacci sequence
2) Given a number F, print out whether it's a fibonacci number and what the closest index n in the 
fibonacci sequence is.
'''
import argparse
import textwrap
import math


def main():
    args = get_args()
    print(type(args))
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
        if is_fibonacci(args.Number):
            position = find_fibonacci_position(args.Number)[1]
            if args.verbose:
                print(
                    f"{args.Number} is at the {position}{get_ord_sufx(position)} position in the Fibonacci sequence.")
            else:
                print(
                    f"True, ({position}{get_ord_sufx(position)}: {args.Number})")
        else:
            closest = find_fibonacci_position(args.Number)
            if args.verbose:
                print(
                    f"{args.Number} is not in the Fibonacci sequence," +
                    f" the closest Fibonacci number is {closest[0]} at the {closest[1]}{get_ord_sufx(closest[1])} index.")
            else:
                print(
                    f"False, ({closest[1]}{get_ord_sufx(closest[1])}: {closest[0]})")


def get_nth_fibonacci(n: int) -> int:
    """Return the number at the nth position in the Fibonacci sequence.

    Args:
        n (int): The position(1-based) in the sequence

    Returns:
        int: A Fibonacci number
    """
    gen = generate_fibonacci()
    # discard range(n - 1) fibonacci numbers
    for _ in range(n - 1):
        next(gen)
    return next(gen)[0]


def is_fibonacci(n: int) -> bool:
    """Check whether n is a Fibonacci number or not applying the Binet's formula.

    Args:
        n (int): The number to check

    Returns:
        bool: :)
    """
    a = 5 * (n ** 2) + 4
    int_sqrt_a = int(math.sqrt(a))
    int_a = int_sqrt_a ** 2

    b = 5 * (n ** 2) - 4
    int_sqrt_b = int(math.sqrt(b))
    int_b = int_sqrt_b ** 2

    return int_a == a or int_b == b


def find_fibonacci_position(n: int) -> tuple:
    """Given n, find the position in the Fibonacci sequence or the closest Fibonacci number

    Args:
        n (int): The number to search

    Returns:
        tuple: ([0]: Closest Fibonacci number, [1]: its position in the sequence)
    """
    gen = generate_fibonacci()
    fib_last = next(gen)

    while fib_last[0] < n:
        fib_prev = fib_last
        fib_last = next(gen)
    # find the closest one
    difference_prev = abs(fib_prev[0] - n)
    difference_last = abs(fib_last[0] - n)

    if difference_last < difference_prev:
        return fib_last
    return fib_prev


# --- Helper functions ---

def generate_fibonacci() -> tuple:
    """Generate the Fibonacci sequence

    Yields:
        Iterator[tuple]: ([0]: The next Fibonacci number, [1]: its position in the sequence)
    """
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


def check_positive(number: str) -> int:
    """ A helper function to validate user input. """
    if int(number) < 0:
        raise argparse.ArgumentTypeError("Not a valid int >= 0")
    return int(number)


def get_args():
    """Parse the command line arguments.

    Returns:
        class 'argparse.Namespace': An object containing the parsed and validated command line arguments.
    """
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


def get_ord_sufx(number: int) -> str:
    """Get the suffix for ordinal numbers. E. g.: 'th' for '12th', 'st' for '1st'

    Args:
        number (int): 

    Returns:
        str: 'th', 'st', 'nd' or 'rd'
    """
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
