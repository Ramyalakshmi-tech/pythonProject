from collections import Counter

str1 = input("Please enter a sentence: ")
words = str1.split(' ')
c = Counter(words)
unique = [w for w in words if c[w] == 1]

print("Unique words: ", unique)