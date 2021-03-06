def cont_fraction(d1: int, d2: int):
    if d2 == 0:
        raise ZeroDivisionError('d2 should not be zero')

    def next_item(number1: int, divide1: int):
        return number1 // divide1, divide1, number1 % divide1

    while d2 > 0:
        r, d1, d2 = next_item(d1, d2)
        yield r
