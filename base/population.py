from typing import List, Type

from base.individual import Individual
from base.item import Item
from base.types import Genome
from crossovers.crossover import Crossover
from crossovers.one_point_crossover import OnePointCrossover
from genome_generators.greedy_genome_generator import GreedyGenomeGenerator
from genome_generators.random_genome_generator import RandomGenomeGenerator
from mutators.inversion_mutator import InversionMutator
from mutators.mutator import Mutator
from mutators.random_mutator import RandomMutator
from selections.roulette_wheel_selection import RouletteWheelSelection
from selections.selection import Selection
from share.check_probability import check_probability


class Population:
    def __init__(self,
                 items: List[Item],
                 capacity: float,
                 size: int,
                 mutation_rate: float = 0.5,
                 selection: Type[Selection] = RouletteWheelSelection,
                 crossover: Type[Crossover] = OnePointCrossover,
                 mutator: Type[Mutator] = InversionMutator,
                 debug=False
                 ):
        self.__items = items
        self.__capacity = capacity
        self.__size = size
        self.__population: List[Individual] = []
        self.__generation_number = 0
        self.__stagnation_count = 0
        self.__last_best_fitness = -1
        self.__selection = selection(items=self.__items)
        self.__crossover = crossover(items=self.__items, capacity=self.__capacity)
        self.__mutator = mutator(items=self.__items, capacity=self.__capacity)
        self.__mutation_rate = mutation_rate

        self.__debug = debug

        self.__generate_initial_individuals()

    def get_the_best(self):
        if len(self.__items) == 0:
            return None

        the_best = self.__population[0]
        max_fitness = the_best.fitness()

        for individual in self.__population:
            fitness = individual.fitness()
            if fitness > max_fitness:
                max_fitness = fitness
                the_best = individual

        return the_best

    def get_generation_number(self):
        return self.__generation_number

    def get_stagnation_count(self):
        return self.__stagnation_count

    def get_average_genome(self):
        average = [0] * len(self.__items)

        for individual in self.__population:
            for i in range(len(individual.get_genome())):
                average[i] += individual.get_genome()[i]

        return [round(gen / len(self.__population)) for gen in average]

    def find_closest_individual(self, genome: Genome):
        min_distance = None
        closest_index = 0

        for j in range(len(self.__population)):
            distance = 0
            current_genome = self.__population[j].get_genome()
            for i in range(len(current_genome)):
                distance += abs(current_genome[i] - genome[i])

            if min_distance is None or distance < min_distance:
                min_distance = distance
                closest_index = j

        return closest_index, self.__population[closest_index]

    def next_generation(self):
        # Скрещивание
        parent_indices = self.__select()
        parents = [self.__population[i] for i in parent_indices]
        children = self.__crossover.cross(parents=parents)

        self.__population += children

        # Мутация
        if check_probability(self.__mutation_rate):
            index, usual_individual = self.find_closest_individual(self.get_average_genome())
            mutated_individual = self.__mutator.mutate(usual_individual)
            self.__population.append(mutated_individual)

        # Удаление лишних
        num_individuals = abs(len(self.__population) - self.__size)
        # selected_indices = self.__selection.select(population=self.__population,
        #                                            num_individuals=num_individuals,
        #                                            reverse_probability=True)

        def find_n_smallest_indices(arr, n):
            # Создаем список индексов от 0 до len(arr)-1
            idxs = list(range(len(arr)))
            # Сортируем список индексов по значению элементов arr
            idxs.sort(key=lambda i: arr[i])
            # Возвращаем первые n индексов
            return idxs[:n]

        selected_indices = find_n_smallest_indices([i.fitness() for i in self.__population], num_individuals)

        for index in sorted(selected_indices, reverse=True):
            del self.__population[index]

        # Обновление статистики
        self.__update_stats()
        # Логирование
        if self.__debug:
            self.__log()

    def __select(self):
        return self.__selection.select(population=self.__population)

    def __generate_initial_individuals(self):
        for i in range(self.__size):
            generator = GreedyGenomeGenerator if check_probability(0.5) else RandomGenomeGenerator
            self.__population.append(Individual(capacity=self.__capacity, items=self.__items, Generator=generator))

    def __update_stats(self):
        self.__generation_number += 1
        best_fitness = self.get_the_best().fitness()

        if self.__last_best_fitness == best_fitness:
            self.__stagnation_count += 1
        else:
            self.__last_best_fitness = best_fitness
            self.__stagnation_count = 0

    def __log(self):
        print(f'=========== [Generation {self.__generation_number}] ===========')
        print(self.get_the_best())
