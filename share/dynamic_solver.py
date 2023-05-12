from typing import List

from base.item import Item


def knapsack_dynamic_programming(items: List[Item], capacity: int):
    n = len(items)
    table = [[0 for _ in range(capacity + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            price = items[i - 1].get_price()
            weight = items[i - 1].get_weight()
            if weight > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], table[i - 1][j - weight] + price)

    selected_items = []
    j = capacity

    for i in range(n, 0, -1):
        if table[i][j] != table[i - 1][j]:
            price = items[i - 1].get_price()
            weight = items[i - 1].get_weight()
            selected_items.append((price, weight))
            j -= weight

    selected_items.reverse()
    total_price = table[n][capacity]

    return selected_items, total_price
