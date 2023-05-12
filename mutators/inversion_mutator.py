import random
from typing import List

from base.individual import Individual
from base.item import Item


class InversionMutator:
    def __init__(self, capacity: float, items: List[Item], mutation_rate: float = 0.5):
        self._mutation_rate = mutation_rate
        self._capacity = capacity
        self._items = items

    def mutate(self, individual: Individual) -> Individual:
        genome = individual.get_genome()
        if random.random() < self._mutation_rate:
            start = random.randint(0, len(genome) - 1)
            end = random.randint(start, len(genome) - 1)
            genome[start:end+1] = reversed(genome[start:end+1])

        mutated_individual = Individual(capacity=self._capacity, items=self._items, genome=genome)
        if not mutated_individual.is_valid_genome():
            mutated_individual.make_it_valid()

        return mutated_individual
