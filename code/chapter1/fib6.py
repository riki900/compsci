"""
Fibonicci sequence generator
will return all fib numbers up to n
"""

from typing import Generator

def fib6(n: int) -> int:
    # first call 
    yield 0
    if n > 0:
        yield 1
    
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
        yield next

 

if __name__ == "__main__":
    for i in fib6(8):
        print(i)

