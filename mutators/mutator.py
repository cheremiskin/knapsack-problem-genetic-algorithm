from typing import List

from base.individual import Individual
from base.item import Item
from share.check_probability import check_probability


class Mutator:
    def __init__(self, capacity: float, items: List[Item], mutation_rate: float = 0.5):
        self._mutation_rate = mutation_rate
        self._capacity = capacity
        self._items = items

    def mutate(self, individual: Individual) -> Individual:
        pass
