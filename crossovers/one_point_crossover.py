import random
from typing import List

from base.individual import Individual
from base.item import Item
from crossovers.crossover import Crossover


class OnePointCrossover(Crossover):
    def __init__(self, capacity: float, items: List[Item]):
        super().__init__(capacity, items)

    def cross(self,  parents: [Individual, Individual]) -> [Individual, Individual]:
        crossover_point = random.randint(0, len(parents[0].get_genome()) - 1)

        children = []
        for i in range(2):
            genome = parents[i].get_genome()[:crossover_point] + parents[1 - i].get_genome()[crossover_point:]
            children.append(Individual(genome=genome, capacity=self._capacity, items=self._items))

        for child in children:
            child.make_it_valid()

        return children
