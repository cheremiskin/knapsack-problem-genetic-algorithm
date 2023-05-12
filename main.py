from solvers.dynamic_solver import DynamicSolver
from solvers.genetic_solver import GeneticSolver
from share.read_input import read_input

if __name__ == '__main__':
    items, capacity = read_input()

    if capacity is None or len(items) < 1:
        raise Exception('bad input')

    # Код для подбора оптимальных параметров
    # optimizer = Optimizer(items=items, capacity=capacity)
    # optimizer.optimize()

    genetic_solver = GeneticSolver(items=items,
                                   capacity=capacity,
                                   population_size=500,
                                   max_iterations=1000,
                                   max_stagnating_iterations=50)

    selected_items_ga, price_ga = genetic_solver.solve()

    dynamic_solver = DynamicSolver(items=items,
                                   capacity=capacity)

    selected_items_da, price_da = dynamic_solver.solve()

    print(f'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Solve GA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          f'fitness: {price_ga} \n'
          f'selected_items: {selected_items_ga} \n'
          f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    print(f'\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Solve DP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          f'fitness: {price_da} \n'
          f'selected items: {selected_items_da} \n'
          f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
