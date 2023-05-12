from typing import List, Tuple

from base.item import Item
from base.types import Solve


class Solver:
    def __init__(self, items: List[Item], capacity: int):
        self._items = items
        self._capacity = capacity

    def solve(self) -> Tuple[Solve, int]:
        pass
