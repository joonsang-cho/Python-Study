def generate(t):
    permutation(t, 0, len(t) - 1)


def permutation(text, start, end):
    if start == end:
        print(''.join(text))
        return

    for i in range(start, end + 1):
        text[start], text[i] = text[i], text[start]
        permutation(text, start + 1, end)
        text[start], text[i] = text[i], text[start]

chars = list('aeiou')
generate(chars)
