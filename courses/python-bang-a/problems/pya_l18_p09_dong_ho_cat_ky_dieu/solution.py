s = int(input().strip())
hh = s // 3600
mm = (s % 3600) // 60
ss = s % 60
print(f"{hh:02d}:{mm:02d}:{ss:02d}")
