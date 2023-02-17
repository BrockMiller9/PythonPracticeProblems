def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    new_lst = {}
    for num in nums:
        new_lst[num] = new_lst.get(num, 0)+1
    max_value = max(new_lst.values())

    for (num, freq) in new_lst.items():
        if freq == max_value:
            return num
