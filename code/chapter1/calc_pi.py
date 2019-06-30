"""
    Calc pi
"""

def calc_pi(nterms: int) -> float:
    NUMERATOR: float = 4.0
    INCREMENT: float = 2.0
    FLIPSIGN: float = -1.0
    demoninator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    for _ in range(nterms):
        pi += operation * (NUMERATOR / demoninator)
        print(_,pi,demoninator,operation)
        demoninator += INCREMENT
        operation *= FLIPSIGN

    return pi

if __name__ == "__main__":
    print(calc_pi(4000))


