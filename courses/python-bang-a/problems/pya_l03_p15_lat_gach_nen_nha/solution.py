l, w, d = map(int, input().split())
s_san = (l * 100) * (w * 100)
s_gach = d * d
print(s_san // s_gach)
