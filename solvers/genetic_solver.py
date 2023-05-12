from typing import List

from base.item import Item
from base.population import Population
from base.types import Genome
from solvers.solver import Solver


class GeneticSolver(Solver):
    def __init__(self,
                 items: List[Item],
                 capacity: float,
                 population_size=20,
                 max_iterations=10000,
                 max_stagnating_iterations=50):
        super().__init__(items, capacity)

        self.__max_iterations = max_iterations
        self.__max_stagnating_iterations = max_stagnating_iterations
        self.__population = Population(items=items, capacity=capacity, size=population_size)
        self.__num_steps_unchanged = 0
        self.__last_best_fitness = -1

    def solve(self):
        while self.__should_continue():
            self.__population.next_generation()

        best_individual = self.__population.get_the_best()
        selected_items = self.__genome_to_selected_items(best_individual.get_genome())

        return selected_items, best_individual.fitness()

    def __genome_to_selected_items(self, genome: Genome):
        selected_items = []

        for i in range(len(genome)):
            if genome[i] == 1:
                selected_items.append((self._items[i].get_price(), self._items[i].get_weight()))

        return selected_items

    def __should_continue(self):
        if self.__population.get_generation_number() >= self.__max_iterations:
            return False

        if self.__population.get_stagnation_count() >= self.__max_stagnating_iterations:
            return False

        return True
