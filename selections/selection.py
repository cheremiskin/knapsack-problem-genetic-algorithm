from typing import List

from base.individual import Individual
from base.item import Item


class Selection:
    def __init__(self, items: List[Item]):
        self._items = items

    def select(self, population: List[Individual], num_individuals: int = 2, reverse_probability: bool = False) -> [int, int]:
        pass
