s = input()
words = s.split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
best_word = max(counts, key=counts.get)
print(best_word, counts[best_word])
