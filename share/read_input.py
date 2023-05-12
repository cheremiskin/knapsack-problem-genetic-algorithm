from typing import List

from base.item import Item


def read_input(file_name: str = "input.txt") -> tuple[list[Item], int | None]:
    input_capacity = None
    input_items = []
    with open(file_name) as file:
        for line in file:
            if input_capacity is None:
                input_capacity = int(line)
            else:
                item = line.split()
                price = int(item[0])
                weight = int(item[1])
                input_items.append(Item(price, weight))
    return input_items, input_capacity
