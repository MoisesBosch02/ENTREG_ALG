import sys

if sys.version_info.major != 3 or sys.version_info.minor < 10:
    raise RuntimeError("This program needs Python3, version 3.10 or higher")

from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph

Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]


def read_data(f: TextIO) -> tuple[UndirectedGraph[Vertex], int, int]:
    # TODO: IMPLEMENTAR
    raise NotImplementedError


def process(ug: UndirectedGraph[Vertex], rows: int, cols: int) -> int:
    # TODO: IMPLEMENTAR
    raise NotImplementedError


def show_results(steps: int):
    print(steps)


if __name__ == "__main__":
    ug0, rows0, cols0 = read_data(sys.stdin)
    steps0 = process(ug0, rows0, cols0)
    show_results(steps0)
