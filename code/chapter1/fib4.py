"""
recursion with base case and memoization
this will run but with excessive calls.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 1) + fib4(n - 2)


if __name__ == "__main__":
    print(fib4(6))
    print(fib4(20))
