"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
# >>> with supressor(IndexError):
# ...    [][2]
"""


class Suppress:
    def __init__(self, e):
        self.e = e
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if type == self.e:
            return self


def suppressed():
    with Suppress(ValueError):
        int('string')


suppressed()
#########################################


class Suppress2:
    def __init__(self, e: type):
        self.e = e
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if type == self.e:
            return self


def contextmanager(func):
    def helper(e: type):
        return Suppress2(func(e))

    return helper


@contextmanager
def s(e: type):
    return e


with s(ZeroDivisionError) as err:
    1 / 0

