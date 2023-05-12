import random
from typing import List

from base.item import Item
from base.types import Genome, GenomeValidationFunction
from genome_generators.genome_generator import GenomeGenerator


class RandomGenomeGenerator(GenomeGenerator):
    def __init__(self, items: List[Item], capacity: float):
        super().__init__(items, capacity)

    def generate(self, validation: GenomeValidationFunction) -> Genome:
        genome_length = len(self._items)
        genome = [random.randint(0, 1) for _ in range(genome_length)]

        while not validation(genome):
            genome[random.randint(0, genome_length - 1)] = 0
        return genome
