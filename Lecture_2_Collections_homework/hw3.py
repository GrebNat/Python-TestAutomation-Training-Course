"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List
import itertools


def combinations(*args: List[Any]) -> List[List]:
    # rang = len(args[0])
    # size = rang ** rang
    # res = []
    #
    # for i in range(0, size):
    #     res.append([])
    #
    # for r in range(0, rang):
    #     index = 0
    #     while index < size:
    #         for j in range(0, rang):
    #             for n in range(0, int(rang ** (rang - r) / rang)):
    #                 res[index].append(args[r][j])
    #                 index += 1

    return list(map(lambda x: list(x), list(itertools.product(*args))))