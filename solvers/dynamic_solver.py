from typing import List, Tuple

from base.item import Item
from base.types import Solve
from solvers.solver import Solver


class DynamicSolver(Solver):
    def __init__(self, items: List[Item], capacity: int):
        super().__init__(items, capacity)

    def solve(self) -> Tuple[Solve, int]:
        n = len(self._items)
        table = [[0 for _ in range(self._capacity + 1)] for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, self._capacity + 1):
                price = self._items[i - 1].get_price()
                weight = self._items[i - 1].get_weight()
                if weight > j:
                    table[i][j] = table[i - 1][j]
                else:
                    table[i][j] = max(table[i - 1][j], table[i - 1][j - weight] + price)

        selected_items = []
        j = self._capacity

        for i in range(n, 0, -1):
            if table[i][j] != table[i - 1][j]:
                price = self._items[i - 1].get_price()
                weight = self._items[i - 1].get_weight()
                selected_items.append((price, weight))
                j -= weight

        selected_items.reverse()
        total_price = table[n][self._capacity]

        return selected_items, total_price
