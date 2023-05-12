from typing import List

from base.individual import Individual
from base.item import Item
from mutators.mutator import Mutator
from share.check_probability import check_probability


class RandomMutator(Mutator):
    def __init__(self, capacity: float, items: List[Item]):
        super().__init__(capacity, items)

    def mutate(self, individual: Individual) -> Individual:
        genome = individual.get_genome()
        new_genome = genome.copy()

        for i in range(len(genome)):
            if check_probability(self._mutation_rate):
                new_genome[i] = 1 - new_genome[i]

        mutated_individual = Individual(capacity=self._capacity, items=self._items, genome=new_genome)

        if not mutated_individual.is_valid_genome():
            mutated_individual.make_it_valid()

        return mutated_individual
