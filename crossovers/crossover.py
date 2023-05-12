from typing import List

from base.individual import Individual
from base.item import Item


class Crossover:
    def __init__(self, capacity: float, items: List[Item]):
        self._capacity = capacity
        self._items = items

    def cross(self, parents: [Individual, Individual]) -> [Individual, Individual]:
        pass
