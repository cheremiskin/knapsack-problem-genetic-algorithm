import random
from typing import List

from base.item import Item
from base.types import GenomeValidationFunction, Genome
from genome_generators.genome_generator import GenomeGenerator


class GreedyGenomeGenerator(GenomeGenerator):
    def __init__(self, items: List[Item], capacity: float):
        super().__init__(items, capacity)

    def generate(self, validation: GenomeValidationFunction) -> Genome:
        genome_length = len(self._items)
        sorted_items = sorted(self._items, key=lambda item: item.get_price() / item.get_weight(), reverse=True)
        genome = [0] * genome_length
        total_weight = 0

        for item in sorted_items:
            if total_weight + item.get_weight() <= self._capacity:
                index = self._items.index(item)
                genome[index] = 1
                total_weight += item.get_weight()

        while not validation(genome):
            index = random.randint(0, genome_length - 1)
            genome[index] = 0
        return genome
