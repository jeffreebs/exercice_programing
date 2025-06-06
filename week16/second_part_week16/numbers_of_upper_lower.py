def print_letters(strings):
    upper= 0
    lower = 0

    for letter in strings:
        if letter.isupper():
            upper+=1
        elif letter.islower():
            lower += 1
    return upper,lower