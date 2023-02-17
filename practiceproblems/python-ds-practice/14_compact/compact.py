def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_lst = []
    for l in lst:
        if l:
            new_lst.append(l)
    return new_lst


print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
