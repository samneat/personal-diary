def count_words(string):
    if string == '':
        return 0
    else:
        words = string.split(' ')
        return len(words)