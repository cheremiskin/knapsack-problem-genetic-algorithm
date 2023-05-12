from typing import List

from base.item import Item
from base.types import Genome, GenomeValidationFunction


class GenomeGenerator:
    def __init__(self, items: List[Item], capacity: float):
        self._items = items
        self._capacity = capacity

    def generate(self, validation: GenomeValidationFunction) -> Genome:
        pass

