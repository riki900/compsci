"""
    trivial compression of string necleotides to 2 bits
"""
from typing import Dict


class CompressedGene(object):
    def __init__(self, gene: str) -> None:

        self._compression_map: Dict[str, int] = {
            "A": 0b00,
            "C": 0b01,
            "G": 0b10,
            "T": 0b11,
        }

        self._decompression_map: Dict[int, str] = dict(
            [(v, k) for k, v in self._compression_map.items()]
        )
        self._bit_string = self._compress(gene)

    def _compress(self, gene) -> int:
        self._bit_string = 1
        for necleotide in gene.toupper():
            self._bit_string <<= 2
            compressed: int = self._compression_map[necleotide]
            self._bit_string |= compressed

        return compressed


def main():
    gc = CompressedGene("ACGT")
    print("Fini")


if __name__ == "__main__":
    main()
