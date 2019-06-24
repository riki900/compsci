"""
recursion with base case
this will run but with excessive calls.
"""


def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


if __name__ == "__main__":
    print(fib2(1))
    print(fib2(2))
    print(fib2(3))
    print(fib2(4))
