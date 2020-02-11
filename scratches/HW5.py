# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def counting(text):
    d = dict()
    for t in text:
        if t in d:
            d[t] += 1
        else:
            d[t] = 1

    print(d)


if __name__ == '__main__':
    google = 'google.com'
    counting(google)

# def counting(a):
#     b = len(list(set(a)))
#     d = list(set(a))
#     result = []
#     for i in range(0, b+1):
#         if i == b:
#             print(result)
#             break
#         else :
#             c = a.count(d[i])
#             result.append("{char} : {no}".format(char = d[i], no = c))
#             i += 1
#
# if __name__ == '__main__':
#     google = 'google.com'
#     counting(google)
