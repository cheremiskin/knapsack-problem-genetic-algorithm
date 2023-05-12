import random
from typing import List, Type

from base.item import Item
from base.types import Genome
from genome_generators.genome_generator import GenomeGenerator
from genome_generators.random_genome_generator import RandomGenomeGenerator


class Individual:
    def __init__(self, capacity: float, items: List[Item], Generator: Type[GenomeGenerator] = RandomGenomeGenerator, genome: Genome = None,):
        self.__capacity = capacity
        self.__items = items

        if genome is not None:
            self.__genome = genome
        else:
            generator = Generator(items=self.__items, capacity=self.__capacity)
            self.__genome = generator.generate(validation=self.is_valid_genome)

    def is_valid_genome(self, genome: Genome = None):
        genome = genome if genome is not None else self.__genome
        return self.get_total_weight(genome) <= self.__capacity

    def fitness(self):
        price_amount = 0
        weight_amount = 0

        for i in range(len(self.__genome)):
            if self.__genome[i] == 1:
                price_amount += self.__items[i].get_price()
                weight_amount += self.__items[i].get_weight()

        if weight_amount > self.__capacity:
            return -1

        return price_amount

    def get_total_weight(self, genome: Genome = None):
        genome = genome if genome is not None else self.__genome
        return sum([genome[j] * self.__items[j].get_weight() for j in range(len(self.__items))])

    def get_genome(self):
        return self.__genome

    def make_it_valid(self):
        while not self.is_valid_genome(self.__genome):
            index = random.randint(0, len(self.__genome) - 1)
            while self.__genome[index] == 0:
                index = (index + 1) % len(self.__genome)

            self.__genome[index] = 0

    def __str__(self):
        return f'fitness: {self.fitness()}, weight: {self.get_total_weight(self.__genome)}, genome: {self.__genome}'
