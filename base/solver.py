from typing import List

from base.item import Item
from base.population import Population


class Solver:
    def __init__(self,
                 items: List[Item],
                 capacity: float,
                 population_size=20,
                 max_iterations=10000,
                 max_stagnating_iterations=50):

        self.__max_iterations = max_iterations
        self.__max_stagnating_iterations = max_stagnating_iterations
        self.__population = Population(items=items, capacity=capacity, size=population_size)
        self.__num_steps_unchanged = 0
        self.__last_best_fitness = -1

    def solve(self):
        while self.__should_continue():
            self.__population.next_generation()

        return self.__population.get_the_best()

    def __should_continue(self):
        if self.__population.get_generation_number() >= self.__max_iterations:
            return False

        if self.__population.get_stagnation_count() >= self.__max_stagnating_iterations:
            return False

        return True
