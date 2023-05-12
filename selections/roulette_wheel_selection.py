import random
from typing import List

from base.individual import Individual
from base.item import Item
from selections.selection import Selection


class RouletteWheelSelection(Selection):
    def __init__(self, items: List[Item]):
        super().__init__(items)

    def select(self, population: List[Individual], num_individuals: int = 2, reverse_probability: bool = False) -> [int, int]:
        fitnesses = [ind.fitness() for ind in population]
        total_fitness = sum(fitnesses)
        probabilities = [fitness / total_fitness for fitness in fitnesses]

        if reverse_probability:
            probabilities = [(1 - p) / (len(population) - 1) for p in probabilities]

        accumulated_probabilities = [sum(probabilities[:i + 1]) for i in range(len(probabilities))]

        selected_indices = []
        for _ in range(num_individuals):
            random_number = random.uniform(0, 1)
            selected_index = None
            for i in range(len(accumulated_probabilities)):
                if random_number < accumulated_probabilities[i]:
                    selected_index = i
                    while selected_index in selected_indices:
                        selected_index = (selected_index + 1) % len(probabilities)
                    break
            if selected_index is None:
                selected_index = len(population) - 1

            selected_indices.append(selected_index)

        return selected_indices
