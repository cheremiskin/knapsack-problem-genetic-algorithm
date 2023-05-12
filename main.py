from base.optimizer import Optimizer
from base.solver import Solver
from share.dynamic_solver import knapsack_dynamic_programming
from share.read_input import read_input

if __name__ == '__main__':
    items, capacity = read_input()

    if capacity is None or len(items) < 1:
        raise Exception('bad input')

    # Код для подбора оптимальных параметров
    # optimizer = Optimizer(items=items, capacity=capacity)
    # optimizer.optimize()

    solver = Solver(items=items,
                    capacity=capacity,
                    population_size=500,
                    max_iterations=1000,
                    max_stagnating_iterations=50)

    solve = solver.solve()
    genome = solve.get_genome()
    selected_items_ga = []

    for i in range(len(genome)):
        if genome[i] == 1:
            selected_items_ga.append((items[i].get_price(), items[i].get_weight()))

    print(f'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Solve GA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          f'fitness: {solve.fitness()} \n'
          f'selected_items: {selected_items_ga} \n'
          f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    selected_items, total_price = knapsack_dynamic_programming(items, capacity)
    print(f'\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Solve DP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          f'fitness: {total_price} \n'
          f'selected items: {selected_items} \n'
          f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
