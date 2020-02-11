# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white


a = list(map(int, input().split(', ')))
print(sorted(list(set(a))))