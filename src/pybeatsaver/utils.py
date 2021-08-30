import re
from typing import *


def split(values: List[any], chunk_size: int) -> Iterator[List[any]]:
    for index in range(0, len(values), chunk_size):
        yield values[index:index + chunk_size]


def camel_to_snake(name: str) -> str:
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)

    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def to_snake_case(name: str) -> str:
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('__([A-Z])', r'_\1', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)

    return name.lower()


def get_args_names(fn) -> List[str]:
    name = list(fn.__code__.co_varnames[:fn.__code__.co_argcount])
    name.remove("self")
    return name
