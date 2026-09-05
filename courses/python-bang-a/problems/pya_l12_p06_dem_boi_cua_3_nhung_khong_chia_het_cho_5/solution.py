a, b = map(int, input().split())
dem3 = b // 3 - (a - 1) // 3
dem15 = b // 15 - (a - 1) // 15
print(dem3 - dem15)
