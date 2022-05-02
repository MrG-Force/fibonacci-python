# The Fibonacci number sequence
### Summary 
This CLI performs two main operations:
1) Given n, get the nth number in the fibonacci sequence.
2) Given a number F, print out whether it's a fibonacci number and what the closest index n in the 
fibonacci sequence is.
"Binet's formula provides a proof that a positive integer x is a Fibonacci number if and only if at least one of 
5 * x * x + 4 or 5 * x * x - 4 is a perfect square". 
Source:
https://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers

The Fibonacci sequence is defined as follows

- The first element is 0
- The second element is 1
- The n<sup>th</sup> element is the sum of the (n-1)<sup>th</sup> and (n-2)<sup>th</sup> elements.

Therefore, the first 21 Fibonacci numbers are:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765
```
### Usage
```
fibonacci.py [-h] (-f | -c) [-v] Number

This program has two main functionalities:
    1. Given an index n (1-based), return the corresponding number at the nth position in the Fibonacci sequence.
        e.g.: fibonacci.py 4 --find -> 2.
    2. Given a number n, determine whether it is a fibonacci number and, if not, find what is the closest index
    in the fibonacci sequence.
        e.g.: fibonacci.py 54 --check -> "False, ('11th': 55)"

positional arguments:
  Number         An integer

optional arguments:
  -h, --help     show this help message and exit
  -f, --find     To find a number at the given position in the Fibonacci sequence
  -c, --check    To determine whether n is a Fibonacci number
  -v, --verbose  Display a verbose output
  ```
