def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    res = []

    for val in lst:
        if isinstance(val, list):
            res.append('True')
        elif val != isinstance(val, list):
            res.append('False')

    if 'False' in res:
        return False
    else:
        return True


print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))
