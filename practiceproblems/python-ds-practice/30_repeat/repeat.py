def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    new_phrase = ''
    while num > 0:
        new_phrase += phrase
        num -= 1
    return new_phrase


print(repeat('*', 3))
print(repeat('abc ', 5))
