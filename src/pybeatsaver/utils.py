from typing import *


def split(values: List[any], chunk_size: int) -> Iterator[List[any]]:
    for index in range(0, len(values), chunk_size):
        yield values[index:index + chunk_size]
