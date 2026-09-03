s = input()
words = s.split()
longest = max(words, key=len)
print(longest)
