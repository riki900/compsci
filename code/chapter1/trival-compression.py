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
        self._compress(gene)

    def _compress(self, gene):
        self._bit_string = 1
        for necleotide in gene.upper():
            self._bit_string <<= 2
            compressed: int = self._compression_map[necleotide]
            self._bit_string |= compressed


    def _decompress(self) -> str:
        gene: str = ""
        # uncompress will built in reverse order
        for i in range(0, self._bit_string.bit_length() - 1, 2):
            bits: int = self._bit_string >> i & 0b11
            gene += self._decompression_map[bits]

        # return string in correct order
        return gene[::-1]

    def __str__(self) -> str:
        return self._decompress()


def main():
    testgene: str = "ACGT"
    gc = CompressedGene(testgene)
    assert testgene == str(gc)
    print('Terminado - OK')


if __name__ == "__main__":
    main()
