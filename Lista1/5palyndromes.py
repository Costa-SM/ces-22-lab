def is_palyndrome(word):
    """
    :param word: possible palyndrome.
    :type word: string.
    :rtype: boolean.
    """
    # set return boolean
    palyndrome = True

    # cast the division to int, so that it can generate a range
    for i in range(int(len(word) / 2)):
        if word[i] != word[len(word) - i - 1]:
            palyndrome = False
            break

    return palyndrome

word = input('Please enter a word: ')

if is_palyndrome(word):
    print('This word is a palyndrome.')
else:
    print('This word is not a palyndrome.')