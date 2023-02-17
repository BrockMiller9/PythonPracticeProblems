def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    total = 0
    for w in word:
        if w.lower() == letter.lower():
            total += 1
    return total


print(single_letter_count('Hello', 'h'))