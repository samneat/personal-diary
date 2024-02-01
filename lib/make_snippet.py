def make_snippet(str):
    list_of_words = str.split(' ')
    if len(list_of_words) > 5:
        first_five = list_of_words[:5]
        snippet = ' '.join(first_five)
        return snippet + '...'
    else:
        return str