from typing import List, Callable, Tuple

Genome = List[int]
GenomeValidationFunction = Callable[[Genome], bool]
Solve = List[Tuple[int, int]]