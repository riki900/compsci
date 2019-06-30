"""
    Towers of Hanoi
"""

recursion_calls: int = 0
max_level = 0


from typing import Generic, TypeVar, List
T = TypeVar('T')

class Stack(Generic[T]):
    
    def __init__(self) -> None:
        self._container: List[T] = [] 

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

def move_disks(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int, level=0) -> None:

    global recursion_calls, max_level

    if level > max_level:
        max_level = level

    recursion_calls += 1
    level += 1 

    if n == 1:
        end.push(begin.pop())
    else:
        move_disks(begin, temp, end, n - 1, level)
        move_disks(begin, end, temp, 1, level)
        move_disks(temp, end, begin, n - 1, level)


def solve_towers_of_hanoi(num_disks) -> None:

    global recursion_calls, max_level
    recursion_calls = 0
    max_level = 0

    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()

    for disk in range(1, num_disks + 1):
        tower_a.push(disk)

    move_disks(tower_a, tower_b, tower_c, num_disks)

    print(tower_a)
    print(tower_b)
    print(tower_c)
    print(f'num disks: {num_disks}, max_level: {max_level} num recursion calls: {recursion_calls}')
    print()


if __name__ == "__main__":
    for num_disks in range(1,10):
        solve_towers_of_hanoi(num_disks)
    
    print()
    print('terminado - OK')