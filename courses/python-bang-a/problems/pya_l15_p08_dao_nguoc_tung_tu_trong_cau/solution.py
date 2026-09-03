s = input()
words = [w[::-1] for w in s.split()]
print(" ".join(words))
