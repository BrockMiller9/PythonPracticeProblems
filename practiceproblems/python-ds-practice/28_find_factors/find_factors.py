def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    numbers = list(range(1, num+1))
    res = []
    for number in numbers:
        # print(number)
        if num % number == 0:
            res.append(number)

    return res


print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
print(find_factors(321421))
