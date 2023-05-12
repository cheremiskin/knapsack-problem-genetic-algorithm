from typing import List

from base.item import Item
from solvers.genetic_solver import Solver


class Optimizer:
    def __init__(self, items: List[Item], capacity: float):
        self.__items = items
        self.__capacity = capacity

    def optimize(self):
        best = [0, 0, 0]
        best_average = 0
        for population_size in range(100, 1000, 100):
            for max_iterations in range(500, 1000, 100):
                for max_stagnating_iterations in range(50, 100, 10):
                    total = 0
                    attempts = 500
                    for attempt in range(attempts):
                        print(attempt)
                        solver = Solver(items=self.__items,
                                        capacity=self.__capacity,
                                        population_size=population_size,
                                        max_iterations=max_iterations,
                                        max_stagnating_iterations=max_stagnating_iterations)
                        the_best = solver.solve()
                        total += the_best.fitness()
                    average = total / attempts
                    if average > best_average:
                        best = [population_size, max_iterations, max_stagnating_iterations]
                        best_average = average
                    print(f'population_size: {population_size}\n'
                          f'max_iterations: {max_iterations}\n'
                          f'max_stagnating_iterations: {max_stagnating_iterations}\n'
                          f'average: {average}\n')

        print(f'======== BEST ========\n'
              f'best: {best}\n'
              f'best average: {best_average}\n')