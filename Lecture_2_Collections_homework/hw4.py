"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable

cashed_params = []


def cache(func: Callable) -> Callable:
    def func_decorator(*some):
        if some not in list(map(lambda x: dict.get(x, "param"), cashed_params)):
            res = func(*some)
            cashed_params.append({"param": some, "result": res})
            return res
        else:
            return dict.get(list(filter(lambda x: dict.get(x, "param") == some, cashed_params))[0], "result")

    return func_decorator
